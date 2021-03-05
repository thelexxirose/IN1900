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


class Cooling:
    def __init__(self, h, T_s):
        self.h = h
        self.T_s = T_s

    def __call__(self, T, t):
        return -self.h*(T - self.T_s)


def estimate_h(t1, Ts, T0, T1):
    return (T1 - T0)/(t1*(Ts - T0))


def test_Cooling():
    c = Cooling(1, 1)
    calculated = c(1, 0)
    expected = 0
    e = 10e-10
    assert abs(calculated - expected) < e


test_Cooling()

time_points = np.linspace(0, 3000, 101)
Ts = [20, 25]

for i in Ts:
    h = estimate_h(15, i, 95, 92)
    cooling = Cooling(h, i)
    mid_euler = MidpointEuler(cooling)
    mid_euler.set_initial_condition(95)
    u, t = mid_euler.solve(time_points)
    plt.plot(t, u, label=f"Ts = {i}")


plt.xlabel("Time(s)")
plt.ylabel("Temp(C)")
plt.legend()
plt.savefig("coffee.png")
plt.show()

'''
(base) corybalaton@Corys-MacBook-Pro Uke 47 %
/usr/local/bin/python3
"/Users/corybalaton/Documents/UiO/IN1900/Uke 47/coffee.py"
'''
