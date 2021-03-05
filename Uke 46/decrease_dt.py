from ForwardEuler_v1 import ForwardEuler_v1
import numpy as np
import matplotlib.pyplot as plt


def x_prime(x, t): return np.cos(6*t)/(1+t+x)


N = [20, 30, 35, 40, 50, 100, 1000, 10000]
X0 = 0
T = 10

for i in N:
    x_arr, t_arr = ForwardEuler_v1(x_prime, X0, T, i).solve()

    plt.plot(t_arr, x_arr, label=f"steps = {i}")

plt.legend()
plt.savefig("decrease_dt.png")
plt.show()
