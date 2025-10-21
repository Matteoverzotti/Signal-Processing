import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2)
fig.suptitle('Exercitiul 4')
axs[0].grid(True)
axs[1].grid(True)
axs[0].set_title('Semnale independente')
axs[1].set_title('Semnale adunate')

A = 1
FREQ_SIN = 70
FREQ_SAWTOOTH = 10
t = np.linspace(0, 1, 1000)

sin = 0.3 * np.sin(2 * FREQ_SIN * np.pi * t)
sawtooth = 2 * (t * FREQ_SAWTOOTH - np.floor(0.5 + t * FREQ_SAWTOOTH))

axs[0].plot(t, sin, label='Sinusoidal')
axs[0].plot(t, sawtooth, label='Sawtooth')
axs[0].legend()

axs[1].plot(t, sin + sawtooth, label='Sum of Sinusoidal and Sawtooth', color='purple')
axs[1].legend()
# plt.show()

plt.savefig('ex4.pdf', format='pdf')