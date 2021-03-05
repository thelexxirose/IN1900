import math as m


def N_of_t(B, k, t, N_0):
    # Calculates C given N(0)
    C = B/N_0 - 1
    # print("C is: " + str(C))
    # Returns N(t)
    return (B/(1 + C*(m.exp(-k*t))))


# Create the structure of the lists
tN1 = [
    [],
    []
]
tN2 = []

# Function for tN1 to generate data


def lists1(B, k, N_0, n):
    for i in range(0, 49, n + 1):
        tN1[0].append(i)
        tN1[1].append(N_of_t(50000, 0.2, i, 5000))


lists1(50000, 0.2, 5000, 12)

# Function for tN2 to generate data


def lists2(B, k, N_0, n):
    for i in range(0, 49, n + 1):
        tN2.append([i, N_of_t(50000, 0.2, i, 5000)])


lists2(50000, 0.2, 5000, 12)

# Formatting of the tables
print("|======METHOD 1======|")


for idx, i in enumerate(tN1[0]):
    print(f'|  t: {i:2d},  N: {int(tN1[1][idx]):5d}  |')


print("|======METHOD 2======|")


for idx, i in enumerate(tN2):
    print(f'|  t: {i[0]:2d},  N: {int(i[1]):5d}  |')

print("|====================|")


'''
(base) corybalaton@Corys-MBP Uke 36 % python3 population_table2.py
|======METHOD 1======|
t:  0,  N:  5000
t: 13,  N: 29967
t: 26,  N: 47634
t: 39,  N: 49816
|======METHOD 2======|
t:  0,  N:  5000
t: 13,  N: 29967
t: 26,  N: 47634
t: 39,  N: 49816
'''
