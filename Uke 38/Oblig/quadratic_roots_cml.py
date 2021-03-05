from math import sqrt
import sys


def quadratic_roots_input(a, b, c):
    x_1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x_2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)

    return (f"The roots are: {x_1} and {x_2}")


print(quadratic_roots_input(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))

'''
(base) corybalaton@Corys-MacBook-Pro Oblig % /Users/corybalaton/opt/anaconda3/bin/python "/Users/corybalaton/Documents/UiO/IN1900/Uke 38/Oblig/quadratic_roots_cml.py" 1 0 -1
The roots are: 1.0 and -1.0
'''
