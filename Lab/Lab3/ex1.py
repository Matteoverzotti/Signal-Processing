import numpy as np
import matplotlib.pyplot as plt

F = [[ np.exp(-2j * np.pi * k * n / 8) for n in range(8) ] for k in range(8) ]
F = np.array(F)

fig, axs = plt.subplots(8)

for i in range(8):
    axs[i].grid(True)
   
    # axs[i].scatter(range(8), F[i].real)
    # axs[i].scatter(range(8), F[i].imag)
    axs[i].plot(F[i].real)
    axs[i].plot(F[i].imag)

# plt.show()
plt.savefig('ex1.pdf', format='pdf')

FH = np.conjugate(F).T

assert(np.allclose(FH @ F, 8 * np.eye(8)))
