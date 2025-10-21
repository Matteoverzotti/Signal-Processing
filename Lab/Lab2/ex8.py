import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 2)
fig.suptitle('Exercitiul 8')

# Flatten axs for easier indexing
axs = axs.flatten()
for ax in axs:
    ax.grid(True)

A = 1
FREQ = 1
t = np.linspace(-np.pi / 2, np.pi / 2, 1000)

alpha = 2 * np.pi * FREQ * t
x_t = A * np.sin(alpha)
x_t_taylor = A * alpha
x_t_pade = A * (alpha - 7 * alpha**3 / 60) / (1 + alpha**2 / 20)
eroare_taylor = abs(x_t - x_t_taylor)
eroare_pade = abs(x_t - x_t_pade)

axs[0].plot(t, x_t, 'b', label='Original')
axs[0].plot(t, x_t_taylor, 'r', label='Taylor')
axs[0].plot(t, x_t_pade, 'g', label='Padé')
axs[0].legend()

axs[1].plot(t, eroare_taylor, 'r', label='Eroare Taylor')
axs[1].plot(t, eroare_pade, 'g', label='Eroare Padé')
axs[1].legend()

# Plot errors on log scale
axs[2].plot(t, eroare_taylor, 'r', label='Eroare Taylor (log)')
axs[2].set_yscale('log')
axs[2].legend()

axs[3].plot(t, eroare_pade, 'g', label='Eroare Padé (log)')
axs[3].set_yscale('log')
axs[3].legend()

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
# plt.show()

plt.savefig('ex8.pdf', format='pdf')