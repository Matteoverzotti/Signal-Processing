import numpy as np
import matplotlib.pyplot as plt

N = 1000
t = np.arange(0, N, 1) 

trend = 0.00002 * t ** 2 - 0.0005 * t + 25
A1 = 1.0
A2 = 0.5
f1 = 0.05
f2 = 20
seasonal = A1 * np.sin(2 * np.pi * f1 * t) + A2 * np.sin(2 * np.pi * f2 * t)

noise = np.random.normal(0, 1, N)

y = trend + seasonal + noise

fig, axs = plt.subplots(3, 1, figsize=(10, 8))
axs[0].plot(t, trend, label='Trend', color='blue')
axs[0].set_title('Trend Component')
axs[0].legend()

axs[1].plot(t, seasonal, label='Seasonal', color='orange')
axs[1].set_title('Seasonal Component')
axs[1].legend()

axs[2].plot(t, y, label='Observed Data', color='green')
axs[2].set_title('Observed Data (Trend + Seasonal + Noise)')
axs[2].legend()

for i in range(3):
    axs[i].grid(True)

plt.tight_layout()
plt.savefig('images/time_series.svg', format='svg')

autocorrelation = np.correlate(y - np.mean(y), y - np.mean(y), mode='full') / np.var(y)
autocorrelation = autocorrelation[autocorrelation.size // 2:]

plt.figure(figsize=(10, 4))
plt.plot(autocorrelation, label='Autocorrelation', color='purple')
plt.savefig('images/autocorrelation.svg', format='svg')

p = 100
y1 = y[p:N]
Y = np.zeros((N - p, p))
for i in range(N - p):
    Y[i] = y[i:i + p][::-1]


x = np.linalg.inv(Y.T @ Y) @ Y.T @ y1
y_pred = Y @ x

plt.figure(figsize=(12, 6))
plt.plot(range(len(y)), y, label='Observed Data', color='green')
plt.plot(range(p, len(y)), y_pred, label='Predicted Data', color='red', linestyle='--')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('images/predicted_time_series.svg', format='svg')

from sklearn.metrics import mean_squared_error
min_mse = float('inf')
best_m = 1
ms = []
for m in range(1, 400):
    y1 = y[m:N]
    Y = np.zeros((N - m, m))
    for i in range(N - m):
        Y[i] = y[i:i + m][::-1]
    x = np.linalg.inv(Y.T @ Y) @ Y.T @ y1
    y_pred = Y @ x

    mse = mean_squared_error(y1, y_pred)
    ms.append(mse)
    if mse < min_mse:
        min_mse = mse
        best_m = m

plt.figure(figsize=(10, 4))
plt.plot(range(1, 400), ms, label='MSE vs m', color='brown')
plt.savefig('images/mse_vs_m.svg', format='svg')
print(f'Cel mai bun orizont de predictie m: {best_m} cu MSE: {min_mse:.6f}')