import numpy as np
import sounddevice as sd

fs = 44100

FREQ_1 = 400  # Hz
FREQ_2 = 800  # Hz
t = np.linspace(0, 1, fs)
x_t_1 = np.sin(2 * np.pi * FREQ_1 * t)
x_t_2 = np.sin(2 * np.pi * FREQ_2 * t)
signal = np.concatenate((x_t_1, x_t_2))

sd.play(signal, fs)
sd.wait()