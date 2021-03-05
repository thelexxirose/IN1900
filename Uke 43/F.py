from math import sin, cos, pi
import numpy as np
import matplotlib.pyplot as plt


class F:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def __call__(self, x):
        return sin(self.n*x) * cos(self.m*x)


u = F(2, 3)
v = F(4, 2)

x = np.linspace(0, 2*pi, 1001)

u_arr = np.array([u(i) for i in x])
v_arr = np.array([v(i) for i in x])

plt.plot(x, u_arr, label="u(x)")
plt.plot(x, v_arr, label="v(x)")
plt.legend()
plt.savefig("F.png")
plt.show()

'''
(base) corybalaton@Corys-MacBook-Pro Uke 43 %
/Users/corybalaton/opt/anaconda3/bin/python
"/Users/corybalaton/Documents/UiO/IN1900/Uke 43/F.py"
'''
