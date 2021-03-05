import numpy as np
import matplotlib.pyplot as plt
from ODESolver import *


def SEIR(u, t):
    beta = 0.5
    r_ia = 0.1
    r_e2 = 1.25
    lmbda_1 = 0.33
    lmbda_2 = 0.5
    p_a = 0.4
    mu = 0.2

    S, E1, E2, I, Ia, R = u
    N = sum(u)
    dS = -beta*S*I/N - r_ia*beta*S*Ia/N - r_e2*beta*S*E2/N
    dE1 = beta*S*I/N + r_ia*beta*S*Ia/N + r_e2*beta*S*E2/N - lmbda_1*E1
    dE2 = lmbda_1*(1-p_a)*E1 - lmbda_2*E2
    dI = lmbda_2*E2 - mu*I
    dIa = lmbda_1*p_a*E1 - mu*Ia
    dR = mu*(I + Ia)
    return [dS, dE1, dE2, dI, dIa, dR]


def test_SEIR():
    expected = [-0.19583333333333333, -0.13416666666666668, -0.302, 0.3, -0.068, 0.4]
    calculated = SEIR([1, 1, 1, 1, 1, 1], 0)

    e = 1e-10

    for i in range(len(expected)):
        err = abs(expected[i] - calculated[i])
        assert err < e, f"Unexpected value: {calculated[i]}, should be: {expected[i]}"


test_SEIR()


def solve_SEIR(T, dt, S_0, E2_0):
    u = []
    t = []
    steps = int(T/dt)
    steps = [i*dt for i in range(steps)]
    ode_seir = RungeKutta4(SEIR)
    ode_seir.set_initial_condition([S_0, 0, E2_0, 0, 0, 0])
    u, t = ode_seir.solve(steps)
    return u, t


def plot_seir(u, t):
    plt.plot(t, [i[0] for i in u], label="S")
    plt.plot(t, [i[3] for i in u], label="I")
    plt.plot(t, [i[4] for i in u], label="I_a")
    plt.plot(t, [i[5] for i in u], label="R")
    plt.legend()
    plt.show()


u, t = solve_SEIR(100, 1.0, 5e6, 100)

plot_seir(u, t)
