import numpy as np
import matplotlib.pyplot as plt
import time

conv_times = []
fft_times = []
N_values = np.linspace(1, 10000, 1000, dtype=int)

for N in N_values:
    p = np.random.randint(-10, 10, N)
    q = np.random.randint(-10, 10, N)

    start = time.time()
    r_conv = np.convolve(p, q)
    conv_times.append(time.time() - start)

    start = time.time()
    size = len(p) + len(q) - 1
    P = np.fft.fft(p, size)
    Q = np.fft.fft(q, size)
    R_fft = P * Q
    r_fft = np.fft.ifft(R_fft).real
    fft_times.append(time.time() - start)

    # Verificare egalitate
    if not np.allclose(r_conv, r_fft):
        print(f"Discrepancy found for N={N}")
        break

plt.plot(N_values, conv_times, label='Convolution Time')
plt.plot(N_values, fft_times, label='FFT Time')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('images/ex3.svg', format='svg')

