import numpy as np
import matplotlib.pyplot as plt

plt.title('Exercitiul 7')
plt.grid(True)

A = 1
FREQ = 20
t = np.linspace(0, 1, 1000)

x_t = A * np.sin(2 * np.pi * FREQ * t)

x_t_1 = x_t[::4]
x_t_2 = x_t[1::4]

plt.plot(t[::4], x_t_1)
plt.plot(t[::4], x_t_2)
# plt.show()

plt.savefig('ex7.pdf', format='pdf')