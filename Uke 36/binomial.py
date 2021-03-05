import math as m


def binomial_prod(n, k):
    result = 1
    for j in range(1, n-k+1):
        result *= (k + j) / j

    return result


def binomial_formula(n, k):
    return m.factorial(n) / (m.factorial(k)*m.factorial(n-k))


print(binomial_prod(4, 2))
print(binomial_formula(4, 2))
