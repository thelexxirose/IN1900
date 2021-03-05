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


def analytical(t):
    return t*np.cos(t)


t = np.linspace(0, 4*np.pi, 101)
plt.plot(t, analytical(t), label="analytical")

mid_euler = MidpointEuler(lambda u, t: np.cos(t) - t*np.sin(t))
t = np.linspace(0, 4*np.pi, 20)
mid_euler.set_initial_condition(0)
u, t = mid_euler.solve(t)
plt.plot(t, u, label="midpoint euler")

plt.legend()
plt.savefig("Midpoint.png")
plt.show()

'''
(base) corybalaton@Corys-MacBook-Pro Uke 47 %
/usr/local/bin/python3
"/Users/corybalaton/Documents/UiO/IN1900/Uke 47/Midpoint.py"
'''
