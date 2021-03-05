import numpy as np
import matplotlib.pyplot as plt
import sys
from math import cos, tan, sqrt

y0 = float(sys.argv[1])
theta = float(sys.argv[2])
v0 = float(sys.argv[3])

g = 9.82

a = -1.0/(2*v0**2)*g/(cos(theta)**2)
b = tan(theta)
c = y0

x1 = (-b**2 + sqrt(b**2 - 4*a*c)) / 2*a
x2 = (-b**2 - sqrt(b**2 - 4*a*c)) / 2*a

x_max = max(x1, x2)

x = np.linspace(0, x_max, 101)

y = a*x**2 + b*x + c

plt.plot(x, y)
plt.show()
