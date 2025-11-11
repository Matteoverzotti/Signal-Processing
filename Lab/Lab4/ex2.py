import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(4)

t = np.linspace(0, 1, 500)
x = np.sin(2 * np.pi * t * 1)
stems = np.linspace(0, 1, 7, endpoint=False)
x_stems = np.sin(2 * np.pi * stems * 1)


for i in range(0, 4):
    ax[i].stem(stems, x_stems)
    ax[i].grid(True)
    ax[i].plot(t, np.sin(2 * np.pi * t * (1 + i * 7)))

plt.tight_layout()
# plt.show()
plt.savefig('ex2.svg', format='svg')
