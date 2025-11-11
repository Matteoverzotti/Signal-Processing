import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 500)
SAMPLING_FREQ = 300

x = np.sin(2 * np.pi * t * 10)

def animate(frame):
    current_sampling_freq = SAMPLING_FREQ - frame
    
    current_sampling_freq = max(current_sampling_freq, 21)
    
    num_points = int(current_sampling_freq)
    stems = np.linspace(0, 1, num_points, endpoint=False)
    x_stems = np.sin(2 * np.pi * stems * 10)
    
    ax.clear()
    
    ax.plot(t, x, 'b-')
    ax.plot(stems, x_stems, 'ro', markersize=8)
    ax.grid(True)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')
    ax.set_title(f'Sampling Frequency: {current_sampling_freq} Hz')
    ax.set_ylim(-1.2, 1.2)
    

fig, ax = plt.subplots()
anim = FuncAnimation(fig, animate, frames=350, interval=10, repeat=True)
plt.tight_layout()
# plt.show()
anim.save('ex3.gif', writer='pillow', fps=30)
