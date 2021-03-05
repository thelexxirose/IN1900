import numpy as np
import matplotlib.pyplot as plt


class ODESolver:
    def __init__(self, f):
        self.f = f

    def advance(self):
        """Advance solution one time step."""
        raise NotImplementedError  # implement in subclass

    def set_initial_condition(self, U0):
        self.U0 = float(U0)

    def solve(self, time_points):
        self.t = np.asarray(time_points)
        N = len(self.t)
        self.u = np.zeros(N)
        # Assume that self.t[0] corresponds to self.U0
        self.u[0] = self.U0

        # Time loop
        for n in range(N-1):
            self.n = n
            self.u[n+1] = self.advance()
        return self.u, self.t


class MidpointEuler(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t

        dt = t[n+1] - t[n]
        k1 = f(u[n], t[n])
        k2 = f(u[n] + dt/2*k1, t[n] + dt/2)
        unew = u[n] + dt*k2
        return unew


class Heuns(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t

        dt = t[n+1] - t[n]
        k1 = f(u[n], t[n])
        k2 = f(u[n] + dt/2*k1, t[n] + dt/2)
        unew = u[n] + dt*(k1/2 + k2/2)
        return unew


class RK4(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        dt = t[n+1] - t[n]
        dt2 = dt/2.0
        K1 = dt*f(u[n], t[n])
        K2 = dt*f(u[n] + 0.5*K1, t[n] + dt2)
        K3 = dt*f(u[n] + 0.5*K2, t[n] + dt2)
        K4 = dt*f(u[n] + K3, t[n] + dt)
        unew = u[n] + (1/6.0)*(K1 + 2*K2 + 2*K3 + K4)
        return unew


def analytical(t):
    return t*np.sin(t) + 2*np.cos(t)


t_a = np.linspace(0, 8*np.pi, 1001)
plt.plot(t_a, analytical(t_a))


def f(u, t):
    return t*np.cos(t) - 2*np.sin(t)


U0 = 2

met = [[MidpointEuler(f), "midpoint euler"],
       [Heuns(f), "heuns"], [RK4(f), "rk4"]]

for i in met:
    i[0].set_initial_condition(U0)

n = [20, 25, 50, 150]

for i, n in enumerate(n):
    plt.figure(i)
    plt.title(f"time points = {n}")
    plt.plot(t_a, analytical(t_a), label="analytical")
    time_points = np.linspace(0, 8*np.pi, n)
    for j, k in enumerate(met):
        u, t = k[0].solve(time_points)
        plt.plot(t, u, label=met[j][1])
    plt.legend()
    plt.savefig(f"compare_methods_{i+1}.png")


plt.show()

'''
(base) corybalaton@Corys-MacBook-Pro Uke 47 %
/usr/local/bin/python3
"/Users/corybalaton/Documents/UiO/IN1900/Uke 47/compare_methods.py"
'''
