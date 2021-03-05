import matplotlib.pyplot as plt
import numpy as np


def ForwardEuler(f, U0, T, N):
    """Solve u’=f(u,t), u(0)=U0, with n steps until t=T."""
    t = np.zeros(N+1)
    u = np.zeros(N+1)

    u[0] = U0
    t[0] = 0
    dt = T/N

    for n in range(N):
        t[n+1] = t[n] + dt
        u[n+1] = u[n] + dt*f(u[n], t[n])

    return u, t


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

u_arr, t_arr = ForwardEuler(f, U0, T, N)

plt.plot(t_arr, u_arr, label=f"steps = {N}")


plt.legend()
plt.savefig("simple_ODE_func_d.png")

# turning N into an array with various steps to see what happens when we increase the number of steps
N = [10, 15, 20, 30, 40]

for i in N:
    u_arr, t_arr = ForwardEuler(f, U0, T, i)

    plt.plot(t_arr, u_arr, label=f"steps = {i}")

plt.legend()
plt.savefig("simple_ODE_func_f.png")

plt.show()
