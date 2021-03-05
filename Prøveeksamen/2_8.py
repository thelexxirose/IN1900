from math import sqrt, ceil


def is_prime(n):
    upper_limit = ceil(sqrt(n))
    is_p = True
    if n % 2 == 0 or n % 3 == 0:
        is_p = False
        return is_p

    for i in range(3, upper_limit, 2):
        if n % i == 0:
            is_p = False
            return is_p

    return is_p


print(is_prime(7))
print(is_prime(9))
print(is_prime(13))
print(is_prime(4))

'''
print(is_prime(49))
print(is_prime(113))
print(is_prime(331))
print(is_prime(104938))
print(is_prime(23))
print(is_prime(10))
'''
