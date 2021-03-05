import math as m


def N_of_t(B, k, t, N_0):
    # Calculates C given N(0)
    C = B/N_0 - 1
    # Returns N(t)
    return (B/(1 + C*m.e**(-(k*t))))


# Print N(24) with B = 50000, k = 0.2^-1, t = 24, and N(0) = 5000
res = N_of_t(50000, 0.2, 24, 5000)
print(res)

'''
(base) corybalaton@Corys-MBP Uke 35 % python3 population.py
50000.0
'''
