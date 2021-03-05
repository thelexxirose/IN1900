from math import cos


def midpoint(f, x, h):
    return (f(x+h) - f(x-h))/2*h


print(midpoint(lambda x: cos(x), 0, 0.001))
