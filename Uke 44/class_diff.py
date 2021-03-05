from math import sin, cos, pi
from matplotlib.lines import Line2D
import numpy as np
import matplotlib.pyplot as plt


class Diff:
    def __init__(self, f):
        self.f = f

    def diff1(self, x, h):
        return (self.f(x+h) - self.f(x))/h

    def diff2(self, x, h):
        return (self.f(x+h) - self.f(x-h))/(2*h)

    def diff3(self, x, h):
        return (-self.f(x+2*h) + 8*self.f(x+h) - 8*self.f(x-h) + self.f(x-2*h))/(12*h)


d = Diff(lambda x: sin(2*pi*x))
x = np.linspace(-1, 1, 101)
v = np.vectorize(lambda x: 2*pi*cos(2*pi*x))
h_vals = [0.9, 0.6, 0.3, 0.1]

plt.plot(x, v(x), color="black", label="exact derivative")

for i in h_vals:
    plt.plot(x, np.vectorize(d.diff1)(x, i), color="blue")
    plt.plot(x, np.vectorize(d.diff2)(x, i), color="red")
    plt.plot(x, np.vectorize(d.diff3)(x, i), color="green")

custom_lines = [Line2D([0], [0], color="blue", lw=4),
                Line2D([0], [0], color="red", lw=4),
                Line2D([0], [0], color="green", lw=4),
                Line2D([0], [0], color="black", lw=4)]

plt.legend(custom_lines, ["diff1", "diff2", "diff3", "exact derivative"])
plt.savefig("class_diff.png")
plt.show()

'''
(base) corybalaton@Corys-MacBook-Pro Uke 44 % /Users/corybalaton/opt/anaconda3/bin/python "/Users/corybalaton/Documents/UiO/IN1900/Uke 44/class_diff.py"
'''
