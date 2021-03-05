# This program is needed in Problem 6.5 Interpret output from a program.

from math import sin, cos, pi


def f(x):
    return sin(x)


def df_approx(f, x, delta_x):
    return (f(x+delta_x)-f(x))/delta_x
# return (f(x+delta_x)-f(x-delta_x))/(2*delta_x)


x = pi/3
for n in range(1, 20):
    delta_x = 10**(-n)
    calculated = df_approx(f, x, delta_x)
    exact = cos(x)
    rel_err = abs(calculated - exact)/abs(exact)
    abs_err = abs(calculated - exact)

    print(f"delta_x: {delta_x}, df_approx: {calculated}, df_exact: {exact}, \
        abs_error: {abs_err}, rel_error: {rel_err}, n={n}")
