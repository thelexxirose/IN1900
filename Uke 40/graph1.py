import numpy as np
import matplotlib.pyplot as plt


def plotline(p1, p2):
    if p1[0] < p2[0]:
        x = np.linspace(p1[0], p2[0])
        y = p1[1] + ((p2[1] - p1[1])/(p2[0] - p1[0]) * x)
        plt.plot(x, y)
    elif p1[0] == p2[0]:
        plt.vlines(p1[0], min(p1[1], p2[1]), max(p1[1], p2[1]))
    else:
        x = np.linspace(p2[0], p1[0])
        y = p2[1] + ((p1[1] - p2[1])/(p1[0] - p2[0]) * x)
        plt.plot(x, y)


plt.axis([0, 4, -1, 6])
plotline((1, 0), (1, 5))
plotline((0, 4), (4, 4))

plt.savefig("graph1.png")

'''
(base) corybalaton@Corys-MacBook-Pro Uke 40 % /Users/corybalaton/opt/anaconda3/bin/python "/Users/corybalaton/Documents/UiO/IN1900/Uke 40/graph1.py"
'''
