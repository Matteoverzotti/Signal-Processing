import numpy as np
import matplotlib.pyplot as plt

def build_signal(A, FREQ, t):
    return A * np.cos(2 * FREQ * np.pi * t)

N = 200

t = np.linspace(0, 1, N)
x1 = build_signal(1, 5, t)
x2 = build_signal(0.5, 20, t)
x3 = build_signal(0.9, 12, t)
x4 = build_signal(0.3, 80, t)
x = x1 + x2 + x3 + x4

fig, axs = plt.subplots(1, 2)
fig.set_figwidth(10)
fig.set_figheight(5)
axs[0].plot(t, x)
axs[0].set_xlabel('Timp (s)')
axs[0].set_ylabel('x(t)')

# Prepare Fourier Transform
F = [[ np.exp(-2j * np.pi * k * n / N) for n in range(N) ] for k in range(N) ]
F = np.array(F)

# Compute the DFT
X = F @ x
axs[1].stem(range(N // 2), np.abs(X[:N // 2]))
axs[1].set_xlabel('Frecvența (Hz)')
axs[1].set_ylabel(f'$|X(\omega)|$')

plt.savefig('ex3.pdf', format='pdf')