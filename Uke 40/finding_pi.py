import numpy as np


def pi_approx(n, x_0):
    if n == 0:
        return x_0

    s = x_0 - (np.sin(x_0)/np.cos(x_0))
    return pi_approx(n-1, s)


def pi_approx_v2(n, x_0):
    next_num = x_0
    for _ in range(n):
        next_num = x_0 - (np.sin(x_0)/np.cos(x_0))
        x_0 = next_num

    return next_num


print("numpy pi        <==> tail recursion  <==> for loop")
for i in range(5):
    print(f"{np.pi:.13f} <==> {pi_approx(i, 3):.13f} <==> {pi_approx_v2(i, 3):.13f}")


'''
(base) corybalaton@Corys-MacBook-Pro Uke 40 % /Users/corybalaton/opt/anaconda3/bin/python "/Users/corybalaton/Documents/UiO/IN1900/Uke 40/finding_pi.py"
numpy pi        <==> tail recursion  <==> for loop
3.1415926535898 <==> 3.0000000000000 <==> 3.0000000000000
3.1415926535898 <==> 3.1425465430743 <==> 3.1425465430743
3.1415926535898 <==> 3.1415926533005 <==> 3.1415926533005
3.1415926535898 <==> 3.1415926535898 <==> 3.1415926535898
3.1415926535898 <==> 3.1415926535898 <==> 3.1415926535898
'''
