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

axs[0].plot(t, y, label='Observed Data', color='green')
axs[0].set_title('Observed Data (Trend + Seasonal + Noise)')
axs[0].legend()

idx = 1
for alpha in [0.1, 0.5, 0.9]:
    s = np.zeros(N)
    s[0] = y[0]
    for i in range(1, N):
        s[i] = alpha * y[i] + (1 - alpha) * s[i - 1]

    axs[idx].plot(t, y, label='Observed Data', color='lightgray', alpha=0.5)
    axs[idx].plot(t, s, label=f'Exponential Smoothing (alpha={alpha})')
    axs[idx].set_title(f'Exponential Smoothing with alpha={alpha}')
    axs[idx].legend()

    idx += 1

for i in range(4):
    axs[i].grid(True)

plt.tight_layout()
plt.savefig('images/fixed_alpha.svg', format='svg')
