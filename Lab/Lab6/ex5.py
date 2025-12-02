import numpy as np
import matplotlib.pyplot as plt

def rectangular_window(N):
    return np.ones(N)

def hanning_window(N):
    return np.hanning(N)

f = 100
A = 1 
phi = 0
T = 1 / 1000
t = np.arange(0, 1, T)
Nw = 200
signal = A * np.sin(2 * np.pi * f * t + phi)

rect_window = rectangular_window(Nw)
hanning_win = hanning_window(Nw)

signal_rect = signal[:Nw] * rect_window
signal_hanning = signal[:Nw] * hanning_win

plt.figure(figsize=(10, 6))
# plt.plot(t, signal, label='Original Signal', color='gray', alpha=0.5)
plt.plot(t[:Nw], signal_rect, label='Rectangular Window', color='blue')
plt.plot(t[:Nw], signal_hanning, label='Hanning Window', color='orange')
plt.title('Signal with Rectangular and Hanning Windows')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('images/ex5.svg', format='svg') 