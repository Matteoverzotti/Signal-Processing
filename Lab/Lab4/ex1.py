import numpy as np
import matplotlib.pyplot as plt
from time import time

fig, ax = plt.subplots()
ax.set_yscale('log')


def fft(x):
    N = len(x)
    if N <= 1:
        return x

    x_even = x[::2]
    x_odd = x[1::2]
    X_even = fft(x_even)
    X_odd = fft(x_odd)
    factor = np.exp(-2j * np.pi * np.arange(N) / N)
    X = np.zeros(N, dtype=complex)
    for k in range(N // 2):
        X[k] = X_even[k] + factor[k] * X_odd[k]
        X[k + N // 2] = X_even[k] - factor[k] * X_odd[k]

    return X

def get_dft_frequencies(N, x_t):
    start = time()
    n = np.arange(N)
    k = n.reshape((N, 1))
    F = np.exp(-2j * np.pi * k * n / N)
    X_DFT = F @ x_t
    dft_frequencies = []
    for k in range(N // 2):
        if abs(X_DFT[k]) > 1e-6:
            dft_frequencies.append(k)
    end = time()

    return dft_frequencies, end - start

def get_fft_frequencies(N, x_t):
    start = time()
    X_FFT = fft(x_t)
    fft_frequencies = []
    for k in range(N // 2):
        if abs(X_FFT[k]) > 1e-6:
            fft_frequencies.append(k)
    end = time()

    return fft_frequencies, end - start

def get_numpy_fft_frequencies(N, x_t):
    start = time()
    X_NP_FFT = np.fft.fft(x_t)
    numpy_fft_frequencies = []
    for k in range(N // 2):
        if abs(X_NP_FFT[k]) > 1e-6:
            numpy_fft_frequencies.append(k)
    end = time()

    return numpy_fft_frequencies, end - start


# Collect all data points first
N_values = [128, 256, 512, 1024, 2048, 4096, 8192]
dft_times = []
fft_times = []
np_fft_times = []

for N in N_values:
    print("N =", N)
    t = np.arange(0, 1, 1/N)
    x_t = np.cos(2 * np.pi * 5 * t) + 0.5 * np.cos(2 * np.pi * 20 * t)

    dft_freqs, dft_time = get_dft_frequencies(N, x_t)
    fft_freqs, fft_time = get_fft_frequencies(N, x_t)
    np_fft_freqs, np_fft_time = get_numpy_fft_frequencies(N, x_t)

    assert(dft_freqs == fft_freqs == np_fft_freqs)
    
    dft_times.append(dft_time)
    fft_times.append(fft_time)
    np_fft_times.append(np_fft_time)


plt.plot(N_values, dft_times)
plt.plot(N_values, fft_times)
plt.plot(N_values, np_fft_times)

plt.xlabel('N (Number of Samples)')
plt.ylabel('Time (seconds)')
plt.legend(['DFT', 'FFT', 'NumPy FFT'])

plt.tight_layout()
# plt.show()
plt.savefig('ex1.svg', format='svg')
