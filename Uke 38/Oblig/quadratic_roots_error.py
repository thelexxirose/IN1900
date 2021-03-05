from math import sqrt
import sys


def quadratic_roots_input(a, b, c):
    x_1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x_2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)

    return (f"The roots are: {x_1} and {x_2}")


try:
    print(quadratic_roots_input(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
except IndexError:
    l = sys.argv[1:]
    while len(l) < 3:
        if (len(l) <= 0):
            l.append(input("input missing value a: "))
        elif (len(l) <= 1):
            l.append(input("input missing value b: "))
        else:
            l.append(input("input missing value c: "))
    print(quadratic_roots_input(int(l[0]), int(l[1]), int(l[2])))

'''
(base) corybalaton@Corys-MacBook-Pro Oblig % /Users/corybalaton/opt/anaconda3/bin/python "/Users/corybalaton/Documents/UiO/IN1900/Uke 38/Oblig/quadratic_roots_error.py" 2
input missing value b: 0
input missing value c: -4
The roots are: 1.4142135623730951 and -1.4142135623730951
'''
