import numpy as np
import matplotlib.pyplot as plt


def arr(filename):
    delta_x = []
    abs_err = []
    n = []
    with open(filename, "r") as f:
        for line in f:
            data = line.rstrip().split(",")
            delta_x.append(float(data[0].split(":")[1].strip()))
            abs_err.append(float(data[3].split(":")[1].strip()))
            n.append(float(data[5].split("=")[1].strip()))

    return delta_x, abs_err, n


delta_x, abs_err, n = np.array(arr("approx_derivative_sine.txt"))

plt.semilogy(n, delta_x, label="delta_x")
plt.semilogy(n, abs_err, label="abs_err")
plt.legend()
plt.savefig("plot_round_off_error.png")

'''
(base) corybalaton@eduroam-193-157-179-38 Uke 42 %
/Users/corybalaton/opt/anaconda3/bin/python
"/Users/corybalaton/Documents/UiO/IN1900/Uke 42/plot_round_off_error.py"
'''
