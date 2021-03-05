import numpy as np
import matplotlib.pyplot as plt


def oscillation(t, A, k, gamma, m):
    return -((A * np.exp(-gamma*t)) * np.cos(np.sqrt((k/m)*t)))


t_array_1 = np.zeros(101)
y_array_1 = np.zeros(101)
interval = [0, 25]

for i in range(len(t_array_1)):
    t_array_1[i] = interval[0] + ((i*(interval[1]-1)) * (1/(len(t_array_1)-1)))
    y_array_1[i] = oscillation(t_array_1[i], 0.3, 4, 0.15, 9)


def func(t):
    return oscillation(t, 0.3, 4, 0.15, 9)


t_array_2 = np.linspace(0, 25, 101)
y_array_2 = np.vectorize(func)

plt.xlabel("time (s)")
plt.ylabel("position (m)")
plt.plot(t_array_1, y_array_1)
plt.savefig("for_loop")
plt.plot(t_array_2, y_array_2(t_array_2))
plt.savefig("vectorized")

'''
(base) corybalaton@Corys-MacBook-Pro Uke 39 %
/Users/corybalaton/opt/anaconda3/bin/python
"/Users/corybalaton/Documents/UiO/IN1900/Uke 39/oscillating_spring.py"
'''
