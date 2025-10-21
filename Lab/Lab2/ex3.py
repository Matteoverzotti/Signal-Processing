import numpy as np
import sounddevice as sd
import scipy

fs = 44100

# a)
f_signal = 400  # Hz
t = np.linspace(0, 0.03, 160000)
x_t_1 = np.sin(2 * np.pi * f_signal * t)

sd.play(x_t_1, fs)
sd.wait()

# b)
f_signal = 800  # Hz
t = np.linspace(0, 3, 100000)
x_t_2 = np.sin(2 * np.pi * f_signal * t)

sd.play(x_t_2, fs)
sd.wait()


# c) Sawtooth wave
f_signal = 240  # Hz
t = np.linspace(0, 0.03, 160000)
x_t_3 = 2 * (t * f_signal - np.floor(0.5 + t * f_signal))
sd.play(x_t_3, fs)
sd.wait()


# d) Square wave
f_signal = 300  # Hz
t = np.linspace(0, 0.03, 160000)
x_t_4 = np.sign(np.sin(2 * np.pi * f_signal * t))

sd.play(x_t_4, fs)
sd.wait()

scipy.io.wavfile.write('square_wave_300Hz.wav', fs, x_t_4)

rate, x = scipy.io.wavfile.read('square_wave_300Hz.wav')
sd.play(x, rate)
sd.wait()