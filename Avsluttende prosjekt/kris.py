import numpy as np


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
        dS = -self.beta(t)*S*I/self.region[i].population-self.r_ia * \
            self.beta(t)*S*sum1-self.r_e2*self.beta(t)*S*sum2
        dE1 = -dS-E1*self.region[i].lmbda
        dE2 = self.lmbda_1*(1-self.p_a)*E1 - self.lmbda_2*E2
        dI = self.lmbda_2*E2 - self.mu*I
        dIa = self.lmbda_1*self.p_a*E1 - self.mu*Ia
        dR = self.mu*(I + Ia)
        derivative += [dS, dE1, dE2, dI, dIa, dR]
    return derivative
