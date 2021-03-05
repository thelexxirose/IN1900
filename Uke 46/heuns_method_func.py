import numpy as np
import matplotlib.pyplot as plt


def heuns_method(f, U0, T, N):
    t = np.zeros(N+1)
    u = np.zeros(N+1)

    u[0] = U0
    t[0] = 0
    dt = T/N

    for n in range(N):
        t[n+1] = t[n] + dt
        k_1 = f(u[n], t[n])
        k_2 = f(u[n] + dt*k_1, t[n] + dt)
        u[n+1] = u[n] + dt*((k_1 + k_2)/2)

    return u, t


def test_heuns_against_hand_calculations():
    u_arr, t_arr = heuns_method(lambda x, t: 1/x, 1, 4, 8)
    a_4 = 3

    e_4 = abs(a_4 - u_arr[8])

    print(f"equation: x' = t/x, where x(0) = 1")
    print(f"x(4) should be {a_4}. x(4) is {u_arr[8]}. error = {e_4}")


test_heuns_against_hand_calculations()

steps = [i for i in range(1, 5)]

for i in steps:
    u_arr, t_arr = heuns_method(lambda x, t: 1/x, 1, 4, i)

    plt.plot(t_arr, u_arr, label=f"steps = {i}")


t = np.linspace(0, 4, 101)
def x(t): return np.sqrt(2*t + 1)


plt.plot(t, x(t), label="analytical")

plt.legend()
plt.savefig("heuns_method_func.png")
plt.show()
