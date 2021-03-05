import numpy as np
import matplotlib.pyplot as plt


def abs_approx(x, N):
    s = 0
    for i in range(1, N+1):
        s += np.cos((2*i-1)*x)/((2*i - 1)**2)
    return (np.pi/2) + (-4/np.pi * s)


x = np.linspace(-np.pi, np.pi, 101)
y = np.vectorize(abs_approx)

plt.axis([-np.pi, np.pi, 0, np.pi])
for i in range(1, 5):
    plt.plot(x, y(x, i))

plt.plot(x, np.abs(x))

plt.savefig("approx_abs.png")

'''
(base) corybalaton@Corys-MacBook-Pro Uke 40 % /Users/corybalaton/opt/anaconda3/bin/python "/Users/corybalaton/Documents/UiO/IN1900/Uke 40/approx_abs.py"
'''
