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


class ForwardEuler(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t

        dt = t[n+1] - t[n]
        unew = u[n] + dt*f(u[n], t[n])
        return unew


def f(u, t):
    return u/5


forward_euler = ForwardEuler(f)

forward_euler.set_initial_condition(0.1)

time_points = [i for i in range(0, 21, 5)]

u, t = forward_euler.solve(time_points)

plt.plot(t, u, label="timestep = 5")

# plotting the exact function


def exact(t): return 0.1*np.exp(0.2*t)


t = np.linspace(0, 20, 101)

plt.plot(t, exact(t), label="exact")

plt.legend()
plt.savefig("simple_ODE_class_ODESolver_c.png")

plt.clf()


def exact(t): return 0.1*np.exp(0.2*t)


t = np.linspace(0, 20, 101)

plt.plot(t, exact(t), label="exact")

for i in range(4, 60, 10):
    time_points = np.linspace(0, 20, i)
    u, t = forward_euler.solve(time_points)
    plt.plot(t, u, label=f"timestep = {20/i: .2f}")

plt.legend()
plt.savefig("simple_ODE_class_ODESolver_f.png")
plt.show()

'''
(base) corybalaton@Corys-MacBook-Pro Uke 47 %
/usr/local/bin/python3
"/Users/corybalaton/Documents/UiO/IN1900/Uke 47/simple_ODE_class_ODESolver.py"
'''
