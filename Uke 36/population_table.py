import math as m


def N_of_t(B, k, t, N_0):
    # Calculates C given N(0)
    C = B/N_0 - 1
    # print("C is: " + str(C))
    # Returns N(t)
    return (B/(1 + C*(m.exp(-k*t))))


N = []
t = []


def lists(B, k, N_0, n):
    for i in range(0, 49, n + 1):
        N.append(N_of_t(50000, 0.2, i, 5000))
        t.append(i)


lists(50000, 0.2, 5000, 12)

for idx, i in enumerate(N):
    print('t: {:2d},  N: {:5.3f}'.format(t[idx], i))

'''
(base) corybalaton@Corys-MBP Uke 36 % python3 population_table.py
t:  0,  N: 5000.000
t: 13,  N: 29967.715
t: 26,  N: 47634.968
t: 39,  N: 49816.297
'''
