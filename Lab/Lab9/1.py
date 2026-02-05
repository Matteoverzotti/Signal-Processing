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

fig, axs = plt.subplots(4, 1, figsize=(10, 8))
axs[0].plot(t, trend, label='Trend', color='blue')
axs[0].set_title('Trend Component')
axs[0].legend()

axs[1].plot(t, seasonal, label='Seasonal', color='orange')
axs[1].set_title('Seasonal Component')
axs[1].legend()

axs[2].plot(t, noise, label='Noise', color='gray')
axs[2].set_title('Noise Component')
axs[2].legend()

axs[3].plot(t, y, label='Observed Data', color='green')
axs[3].set_title('Observed Data (Trend + Seasonal + Noise)')
axs[3].legend()

for i in range(4):
    axs[i].grid(True)

plt.tight_layout()
plt.savefig('images/time_series.svg', format='svg')
