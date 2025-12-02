import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

N = 100
x = np.random.random(N)
block = np.zeros(N)
block[40:60] = 1


fig, axs = plt.subplots(4, 2, figsize=(8, 12))
for i in range(4):
    axs[i, 0].plot(x)
    axs[i, 0].set_title(f'Iteration {i}: Random Signal')
    axs[i, 0].grid(True)
    x = signal.convolve(x, x)

    axs[i, 1].plot(block)
    axs[i, 1].set_title(f'Iteration {i}: Block Signal')
    axs[i, 1].grid(True)
    block = signal.convolve(block, block)

plt.tight_layout()
plt.savefig('images/ex2.svg', format='svg')