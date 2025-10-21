import matplotlib.pyplot as plt
import numpy as np

# Create a figure with custom grid layout
fig = plt.figure(figsize=(12, 12))
fig.suptitle('Exercitiul 2')

gs = fig.add_gridspec(4, 2, width_ratios=[1, 1.5])

axs = []
for i in range(4):
    ax = fig.add_subplot(gs[i, 0])
    ax.set_xlim(0, 0.03)
    ax.grid(True)
    axs.append(ax)

ax_2d_top = fig.add_subplot(gs[:2, 1])
ax_2d_bottom = fig.add_subplot(gs[2:, 1])

# a)
f_signal = 400  # Hz
t = np.linspace(0, 0.03, 1600)
x_t = np.sin(2 * np.pi * f_signal * t)

axs[0].plot(t, x_t)

# b)
f_signal = 800  # Hz
t = np.linspace(0, 3, 100000)
x_t = np.sin(2 * np.pi * f_signal * t)

axs[1].plot(t, x_t)

# c) Sawtooth wave
f_signal = 400  # Hz
t = np.linspace(0, 0.03, 1600)
x_t = 2 * (t * f_signal - np.floor(0.5 + t * f_signal))

axs[2].plot(t, x_t)

# d) Square wave
f_signal = 400  # Hz
t = np.linspace(0, 0.03, 1600)
x_t = np.sign(np.sin(2 * np.pi * f_signal * t))

axs[3].plot(t, x_t)

# e) Un semnal 2D aleator (top)
random_2d_signal = np.random.rand(128, 128)
im = ax_2d_top.imshow(random_2d_signal)

# f) Un semnal 2D la alegerea voastra (bottom)
choice_2d_signal = np.zeros((128, 128))
for i in range(128):
    for j in range(128):
        choice_2d_signal[i, j] = (i + j) % 256

im2 = ax_2d_bottom.imshow(choice_2d_signal, cmap='viridis', interpolation='nearest')

ax_2d_top.axis('off')
ax_2d_bottom.axis('off')

# Save the figure to eps
plt.show()
fig.savefig('ex2.pdf', format='pdf')
