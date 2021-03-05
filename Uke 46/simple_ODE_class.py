from ForwardEuler_v1 import ForwardEuler_v1
import numpy as np
import matplotlib.pyplot as plt

# u' = u/5


def f(u, t):
    return u/5


# plotting the exact function
def exact(t): return 0.1*np.exp(0.2*t)


t = np.linspace(0, 20, 101)

plt.plot(t, exact(t), label="exact")

# Plotting the equation using forward euler with 5 steps, and saving figure.
U0 = 0.1
N = 5
T = 20

u_arr, t_arr = ForwardEuler_v1(f, U0, T, N).solve()

plt.plot(t_arr, u_arr, label=f"steps = {N}")


plt.legend()
plt.savefig("simple_ODE_class_d.png")

# turning N into an array with various steps to see what happens when we increase the number of steps
N = [10, 15, 20, 30, 40]

for i in N:
    u_arr, t_arr = ForwardEuler_v1(f, U0, T, i).solve()

    plt.plot(t_arr, u_arr, label=f"steps = {i}")

plt.legend()
plt.savefig("simple_ODE_class_f.png")

plt.show()
