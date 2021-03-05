from math import factorial


def cos_approx(x, n):
    s = 0
    for i in range(n+1):
        s += (-1)**i * (x**(2*i)/2*factorial(i))

    return s
