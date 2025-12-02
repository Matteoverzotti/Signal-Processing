import numpy as np
import matplotlib.pyplot as plt

Fs = [1, 1.5, 2, 4] # Hz

B = 1
t = np.linspace(-3, 3, 1000)
x = np.sinc(B * t) ** 2

for plt_index in range(4):
    ax = plt.subplot(2, 2, plt_index + 1)
    ax.plot(t, x, 'black', alpha=0.5)

    samples = np.arange(-3, 3, 1 / Fs[plt_index])

    # Center samples at 0
    offset = samples[np.abs(samples).argmin()]
    samples = samples - offset
    x_samples = np.sinc(B * samples) ** 2
    ax.stem(samples, x_samples, linefmt='orange')

    reconscruct = np.zeros_like(t)
    for n in range(len(samples)):
        reconscruct += x_samples[n] * np.sinc(Fs[plt_index] * (t - samples[n]))
    
    ax.plot(t, reconscruct, 'g--', alpha=1)

    ax.set_title(f'$F_s = {Fs[plt_index]}$ Hz')
    ax.set_xlabel('t[s]')
    ax.set_ylabel('Amplitude')
    ax.grid(True)

plt.tight_layout()
plt.savefig('images/ex1.svg', format='svg')