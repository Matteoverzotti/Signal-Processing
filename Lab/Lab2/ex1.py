import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2)
fig.suptitle('Exercitiul 1')
axs[0].grid(True)
axs[1].grid(True)
axs[0].set_title('Semnal sinusoidal')
axs[1].set_title('Semnal cosinusoidal')


A = 1
FREQ = 10
t = np.arange(0, 1, 0.00001)
x_t_1 = A * np.sin(2 * FREQ * np.pi * t + np.pi / 3)
x_t_2 = A * np.cos(2 * FREQ * np.pi * t + np.pi / 3 - np.pi / 2)

axs[0].plot(t, x_t_1)
axs[1].plot(t, x_t_2)

# plt.show()

plt.savefig('ex1.pdf', format='pdf')