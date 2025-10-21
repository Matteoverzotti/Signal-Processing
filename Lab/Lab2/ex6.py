import numpy as np
import matplotlib.pyplot as plt

plt.title('Exercitiul 6')

A = 1
TIME = 1
fs = 10

t = np.linspace(0, TIME, 1000)

# a) f = fs / 2
x_t_1 = A * np.sin(2 * fs / 2 * np.pi * t)


# b) f = fs / 4
x_t_2 = A * np.sin(2 * fs / 4 * np.pi * t)

# c) f = 0
x_t_3 = A * np.sin(2 * 0 * np.pi * t)

plt.plot(t, x_t_1)
plt.plot(t, x_t_2)
plt.plot(t, x_t_3)
plt.grid(True)
# plt.show()

plt.savefig('ex6.pdf', format='pdf')