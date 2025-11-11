import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import roseus.mpl as rs

filename = "vocals.wav"

sampling_rate, data = wavfile.read(filename)

N = data.shape[0]

frame_size = int(N * 0.01) # 1% din N
hop_size = frame_size // 2
num_frames = (N - frame_size) // hop_size + 1
spectrogram = np.zeros((frame_size // 2 + 1, num_frames))

window = np.hanning(frame_size)

for i in range(num_frames):
    start = i * hop_size
    end = start + frame_size
    frame = data[start:end]
    if frame.shape[0] < frame_size:
        frame = np.pad(frame, (0, frame_size - frame.shape[0]), mode='constant')
    spectrum = np.fft.rfft(frame * window)
    spectrogram[:, i] = np.abs(spectrum)

spectrogram_db = 20 * np.log10(np.maximum(spectrogram, np.max(spectrogram) * 1e-6))

plt.imshow(spectrogram_db, aspect='auto', origin='lower',
              extent=[0, N / sampling_rate, 0, sampling_rate / 2], 
              cmap=rs.roseus, vmin=np.max(spectrogram_db)-80, vmax=np.max(spectrogram_db))
plt.colorbar(label='Magnitude (dB)')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.title('Spectrogram of vocals.wav')
plt.tight_layout()
# plt.show()
plt.savefig('ex6.svg', format='svg')