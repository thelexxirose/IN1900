import matplotlib.pyplot as plt
import numpy as np
from ODESolver import *

# Region class


class Region:
    # Init method
    def __init__(self, name, S_0, E2_0):
        self.name = name
        self.S_0, self.E1_0, self.E2_0, self.I_0, self.Ia_0, self.R_0 = S_0, 0, E2_0, 0, 0, 0
        self.population = sum([self.S_0, self.E1_0, self.E2_0, self.I_0, self.Ia_0, self.R_0])
        self.u = []
        self.t = []

    # Appends an array of 6 values that should correspond to the answers
    def set_SEIR_values(self, u, t):
        for i in u:
            self.u.append(i)
        for i in t:
            self.t.append(i)

    # Plots the S, I1, I2 and R values
    def plot(self):
        plt.xlabel('Time(days)')
        plt.ylabel('Population')
        plt.title(self.name)
        vals = [[0, 'Susceptible'], [3, 'Infectious 1'], [4, 'Infectious 2'], [5, 'Removed']]
        for j in vals:
            plt.plot(self.t, [self.u[i][j[0]] for i in range(len(self.u))], label=j[1])

# A subclass of Region


class ProblemSEIR(Region):
    # init method
    def __init__(self, region, beta, r_ia=0.1, r_e2=1.25, lmbda_1=0.33, lmbda_2=0.5, p_a=0.4, mu=0.2):
        if isinstance(beta, (float, int)):  # number?
            self.beta = lambda t: beta    # wrap as function
        elif callable(beta):
            self.beta = beta
        self.region = region
        self. beta = beta
        self.r_ia = r_ia
        self.r_e2 = r_e2
        self.lmbda_1 = lmbda_1
        self.lmbda_2 = lmbda_2
        self.p_a = p_a
        self.mu = mu

        self.set_initial_condition()

    # Method that sets the initial condition
    def set_initial_condition(self):
        self.initial_condition = [self.region.S_0, self.region.E1_0,
                                  self.region.E2_0, self.region.I_0, self.region.Ia_0, self.region.R_0]

    # Method that returns the total population
    def get_population(self):
        return self.region.population

    # Method that inputs an array of with solutions at a certain time
    def solution(self, u, t):
        self.region.set_SEIR_values(u, t)

    # Call method that calculates the derivatives
    def __call__(self, u, t):
        N = sum(u)
        S, E1, E2, I, Ia, R = u
        dS = -1*self.beta*S*I/N - self.r_ia*self.beta*S*Ia/N - self.r_e2*self.beta*S*E2/N
        dE1 = self.beta*S*I/N + self.r_ia*self.beta*S*Ia/N + self.r_e2*self.beta*S*E2/N - self.lmbda_1*E1
        dE2 = self.lmbda_1*(1-self.p_a)*E1 - self.lmbda_2*E2
        dI = self.lmbda_2*E2 - self.mu*I
        dIa = self.lmbda_1*self.p_a*E1 - self.mu*Ia
        dR = self.mu*(I + Ia)
        return [dS, dE1, dE2, dI, dIa, dR]

# Class that uses the ODESolver to create the solution arrays at times t.


class SolverSEIR:
    # Init method
    def __init__(self, problem, T, dt):
        self.problem = problem
        self.T = int(T)
        self.dt = dt

    # Method that uses the RungeKutta4 method to give solutions at times t
    def solve(self, method=RungeKutta4):
        solver = method(self.problem)
        solver.set_initial_condition(self.problem.initial_condition)
        time_steps = int(self.T/self.dt)
        t = np.linspace(0, self.T, time_steps)
        u, t = solver.solve(t)

        self.problem.solution(u, t)


if __name__ == '__main__':
    nor = Region('Norway', S_0=5e6, E2_0=100)
    problem = ProblemSEIR(nor, beta=0.5)
    solver = SolverSEIR(problem, T=100, dt=1.0)
    solver.solve()
    print(nor.u)
    nor.plot()
    plt.legend()
    plt.show()
