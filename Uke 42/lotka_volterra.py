import numpy as np
import matplotlib.pyplot as plt

F = np.zeros(500)
R = np.zeros(500)

R[0] = 100
F[0] = 20

for i in range(1, 500):
    R[i] = R[i-1] + 0.04*R[i-1] - 0.005*R[i-1]*F[i-1]
    F[i] = F[i-1] + 0.2*0.005*R[i-1]*F[i-1] - 0.1*F[i-1]

x = np.linspace(0, 500, 500)

plt.plot(x, R, label="Rabbits")
plt.plot(x, F, label="Foxes")
plt.xlabel("N")
plt.ylabel("population")
plt.legend()
plt.savefig("lotka_volterra.png")

'''
(base) corybalaton@eduroam-193-157-179-38 Uke 42 %
/Users/corybalaton/opt/anaconda3/bin/python
"/Users/corybalaton/Documents/UiO/IN1900/Uke 42/lotka_volterra.py"
'''
