from SEIR import Region, ProblemSEIR, SolverSEIR
import numpy as np
import matplotlib.pyplot as plt

# Class that is basically like the Region class, except that it takes in a latitude and longitude


class RegionInteraction(Region):
    # Init method
    def __init__(self, name, S_0, E2_0, phi, lmbda):
        super().__init__(name, S_0, E2_0)
        self.phi = phi*np.pi/180
        self.lmbda = lmbda*np.pi/180

    # Method that calculates the distance between to instances of RegionInteraction.
    # Returns the distance expressed as 10^5m
    def distance(self, other):
        R_earth = 64
        t = np.sin(self.phi)*np.sin(other.phi) + np.cos(self.phi) * \
            np.cos(other.phi)*np.cos(abs(self.lmbda - other.lmbda))
        if t <= 0:
            t = 0
        elif t >= 1:
            t = 1
        return R_earth*np.arccos(t)

# Class that is the same as ProblemSeir, only that region is now a list of RegionInteraction instances


class ProblemInteraction(ProblemSEIR):
    def __init__(self, region, area_name, beta, r_ia=0.1, r_e2=1.25, lmbda_1=0.33, lmbda_2=0.5, p_a=0.4, mu=0.2):
        super().__init__(region, beta, r_ia, r_e2, lmbda_1, lmbda_2, p_a, mu)
        self.area_name = area_name
        self.u = []
        self.t = []

    # Method that returns the total population of all the regions within the area
    def get_population(self):
        population = 0
        for i in self.region:
            population += i.population
        return population

    # Method that sets the initial condition of all the regions into a single one-dimensional list
    def set_initial_condition(self):
        self.initial_condition = []
        for i in self.region:
            self.initial_condition += [i.S_0, i.E1_0, i.E2_0, i.I_0, i.Ia_0, i.R_0]

    def __call__(self, u, t):
        n = len(self.region)
        SEIR_list = [u[i:i+6] for i in range(0, len(u), 6)]
        E2_list = [u[i] for i in range(2, len(u), 6)]
        Ia_list = [u[i] for i in range(4, len(u), 6)]
        derivative = []
        for i in range(n):
            S, E1, E2, I, Ia, R = SEIR_list[i]
            sum1 = 0
            sum2 = 0
            for j in range(n):
                E2_other = E2_list[j]
                Ia_other = Ia_list[j]
                pop_other = self.region[j].population
                distance = self.region[i].distance(self.region[j])
                ex = np.exp(-distance)
                sum1 += (Ia_other/pop_other)*ex
                sum2 += (E2_other/pop_other)*ex
            dS = -1*self.beta*S*I/self.region[i].population - \
                self.r_ia*self.beta*S*sum1-self.r_e2*self.beta*S*sum2
            dE1 = -dS-E1*self.region[i].lmbda
            dE2 = self.lmbda_1*(1-self.p_a)*E1 - self.lmbda_2*E2
            dI = self.lmbda_2*E2 - self.mu*I
            dIa = self.lmbda_1*self.p_a*E1 - self.mu*Ia
            dR = self.mu*(I + Ia)
            derivative += [dS, dE1, dE2, dI, dIa, dR]
        return derivative

    def solution(self, u, t):
        n = len(t)
        n_reg = len(self.region)
        self.arr = []
        self.S = np.zeros(n)
        self.E1 = np.zeros(n)
        self.E2 = np.zeros(n)
        self.I = np.zeros(n)
        self.Ia = np.zeros(n)
        self.R = np.zeros(n)
        SEIR_list = [u[:, i:i+6] for i in range(0, n_reg*6, 6)]
        print(SEIR_list)
        for part, SEIR in zip(self.region, SEIR_list):
            part.set_SEIR_values(SEIR, t)
        for i in range(n):
            for j in range(n_reg):
                self.S[i] += SEIR_list[j][i][0]
                self.E1[i] += SEIR_list[j][i][1]
                self.E2[i] += SEIR_list[j][i][2]
                self.I[i] += SEIR_list[j][i][3]
                self.Ia[i] += SEIR_list[j][i][4]
                self.R[i] += SEIR_list[j][i][5]
            self.arr.append([self.S[i], self.E1[i],
                             self.E2[i], self.I[i], self.Ia[i], self.R[i]])

        self.set_SEIR_values(self.arr, t)

    # Plots the S, I1, I2 and R values
    def plot(self):
        plt.xlabel('Time(days)')
        plt.ylabel('Population')
        plt.title(self.area_name)
        vals = [[0, 'Susceptible'], [1, "Exposed 1"], [2, "Exposed 2"],
                [3, 'Infectious 1'], [4, 'Infectious 2'], [5, 'Removed']]
        for j in vals:
            plt.plot(self.t, [self.u[i][j[0]] for i in range(len(self.u))],
                     label=j[1])


if __name__ == "__main__":
    innlandet = RegionInteraction("Innlandet", S_0=371385, E2_0=0,
                                  phi=60.7945, lmbda=11.0680)
    oslo = RegionInteraction("Oslo", S_0=693494, E2_0=100,
                             phi=59.9, lmbda=10.8)
    print(oslo.distance(innlandet))

    s = ProblemInteraction([innlandet, oslo], "s", 0.5)
    print(s.region)
    s.set_initial_condition()

    print(s.initial_condition)
    print(s.get_population())

    problem = ProblemInteraction([oslo, innlandet], "Norway_east", beta=0.5)
    print(problem.get_population())
    problem.set_initial_condition()
    print(problem.initial_condition)  # non-nested list of length 12
    u = problem.initial_condition
    print(problem(u, 0))  # list of length 12. Check that values make sense

    solver = SolverSEIR(problem, T=100, dt=1.0)
    solver.solve()
    problem.plot()
    plt.legend()
    plt.savefig("SEIR_interaction.png")
    plt.show()
