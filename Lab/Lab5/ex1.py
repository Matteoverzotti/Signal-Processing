import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

df = pd.read_csv('Train.csv', parse_dates=[1], dayfirst=True)
N = len(df)

time_diff_hours = (df.iloc[-1, 1] - df.iloc[0, 1]).total_seconds()
fs = 1 / 3600
print(f"Numărul de eșantioane: {N}")
print(f"Frecvență de eșantionare: {fs} Hz")
print(f"Intervalul total de timp: {time_diff_hours} secunde")
print("Interval de timp: ", df.iloc[0, 1], " - ", df.iloc[-1, 1])

signal = df['Count'].to_numpy()

# e) Eliminarea componentei continue
mean_signal = np.mean(signal)
print(f"Valoarea medie a semnalului: {mean_signal}")

X = np.fft.fft(signal)[:N // 2]
X_magnitude = np.abs(X / N)
f = fs * np.linspace(0, N // 2, N // 2) / N

plt.plot(f, X_magnitude)
plt.grid(True)

plt.tight_layout()
plt.savefig('fft_original_magnitude.svg')

dc_component = X_magnitude[0]
print(f"Componenta continuă (DC): {dc_component}")

assert np.isclose(dc_component, mean_signal), "Componenta DC nu este egală cu valoarea medie a semnalului!"

signal_dc_removed = signal - mean_signal
X = np.fft.fft(signal_dc_removed)[:N // 2]
X_magnitude = np.abs(X / N)

plt.plot(f, X_magnitude)
plt.grid(True)

plt.tight_layout()
plt.savefig('fft_magnitude.svg')

# f) Identificarea frecvențelor dominante
top_indices = np.argsort(X_magnitude)[-3:][::-1]
print("Frecvențele dominante și magnitudinile lor:")
for idx in top_indices:
    print(f"Frecvență: {f[idx]:.10f} Hz, Magnitudine: {X_magnitude[idx]:.6f}")


# g) o luna de trafic

start_sample = 1024 # round and pretty
start_date = df.iloc[start_sample, 1]
while start_date.weekday() != 0:  # 0 = luni
    start_sample += 1
    start_date = df.iloc[start_sample, 1]

num_samples_month = 30 * 24  # 30 zile
end_sample = start_sample + num_samples_month
signal_month = signal[start_sample:end_sample]
time_month = df.iloc[start_sample:end_sample, 1]

plt.figure()
plt.plot(time_month, signal_month)
plt.title(f'Trafic pentru o lună începând din {start_date.strftime("%d %B %Y (%A)")}')
plt.xlabel('Data')
plt.ylabel('Numărul de vehicule')
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('trafic_luna.svg')

print(f"Perioada vizualizată: {time_month.iloc[0]} - {time_month.iloc[-1]}")
print(f"Numărul de eșantioane vizualizate: {len(signal_month)}")

# i) Filtrarea semnalului

cutoff_hours = 12
cutoff_frequency = 1 / (cutoff_hours * 3600) # 1/(12 ore) in Hz

X = np.fft.fft(signal)

frequencies = np.fft.fftfreq(N, 1/fs)
X_filtered = X.copy()
X_filtered[np.abs(frequencies) >= cutoff_frequency] = 0
filtered_signal = np.real(np.fft.ifft(X_filtered))

fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
axes[0].plot(signal, label="Semnal original")
axes[0].set_ylabel("Număr mașini")
axes[0].set_title("Semnal inițial")
axes[0].legend()

axes[1].plot(filtered_signal, label="Semnal filtrat")
axes[1].set_ylabel("Număr mașini")
axes[1].set_title("Semnal după filtrare")
axes[1].legend()

plt.tight_layout()
plt.savefig('semnal_filtrat.svg')
