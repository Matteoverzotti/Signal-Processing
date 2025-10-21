import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2)
fig.suptitle('Exercitiul 2')
axs[0].grid(True)
axs[1].grid(True)
axs[0].set_title('Semnale sinusoidale')
axs[1].set_title('Semnal zgomotos')

A = 1
FREQ = 10
t = np.arange(0, 1, 0.001)
x_t_1 = A * np.sin(2 * FREQ * np.pi * t + np.pi * 3 / 4)
x_t_2 = A * np.sin(2 * FREQ * np.pi * t + np.pi * 2)
x_t_3 = A * np.sin(2 * FREQ * np.pi * t + np.pi)
x_t_4 = A * np.sin(2 * FREQ * np.pi * t - np.pi / 2)

z = np.random.normal(0, 1, len(t))

SNR = 100
x_norm = np.linalg.norm(x_t_1) ** 2
z_norm = np.linalg.norm(z) ** 2
gamma = np.sqrt(x_norm / (SNR * z_norm))

axs[0].plot(t, x_t_2)
axs[0].plot(t, x_t_3)
axs[0].plot(t, x_t_4)

axs[1].plot(t, x_t_1 + gamma * z)
axs[1].plot(t, x_t_1)
# plt.show()

plt.savefig('ex2.pdf', format='pdf')