import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(3)
fig.suptitle('Exercitiul 1')

# a)
t = np.arange(0, 0.03, 0.0005)

# b)
x_t = np.cos(520 * np.pi * t + np.pi / 3)
y_t = np.cos(280 * np.pi * t - np.pi / 3)
z_t = np.cos(120 * np.pi * t + np.pi / 3)

# c) Stem them with a 200Hz frequency
fs = 200  # sampling frequency
t_stem = np.arange(0, 0.03, 1/fs)

x_stem = np.cos(520 * np.pi * t_stem + np.pi / 3)
y_stem = np.cos(280 * np.pi * t_stem - np.pi / 3)
z_stem = np.cos(120 * np.pi * t_stem + np.pi / 3)

axs[0].stem(t_stem, x_stem)
axs[1].stem(t_stem, y_stem)
axs[2].stem(t_stem, z_stem)

axs[0].plot(t, x_t)
axs[1].plot(t, y_t)
axs[2].plot(t, z_t)

for ax in axs:
    ax.grid(True)
plt.show()

# Save the figure to eps
fig.savefig('ex1.eps', format='eps')
