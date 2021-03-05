# 8.3 Make a function class

from math import sin, cos, pi
import numpy as np
import matplotlib.pyplot as plt


class F:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def __call__(self, x):
        return sin(self.n * x) * cos(self.m * x)


u = F(2, 4)
v = F(5, 7)

x = np.linspace(0, 2*pi, 1001)
u_arr = [u(i) for i in x]
v_arr = [v(i) for i in x]

plt.plot(x, u_arr, label="u(x)")
plt.plot(x, v_arr, label="v(x)")
plt.legend()
plt.savefig("F.py")
plt.show()
