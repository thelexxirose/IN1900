from math import sqrt

running = True


def quadratic_roots_input():
    a = float(input("input value a: "))
    b = float(input("input value b: "))
    c = float(input("input value c: "))

    x_1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x_2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)

    return (f"The roots are: {x_1} and {x_2}")


while running:
    print(quadratic_roots_input())
    t = False
    run_again = input(
        "Do you want to calculate the roots of another second degree polynomial? (y/n): ")
    if (run_again == "n"):
        running = False
        t = True
    elif (run_again == "y"):
        t = True
    while (not t):
        run_again = input("You have to input either y or n: ")
        if (run_again == "n"):
            running = False
            t = True
        elif (run_again == "y"):
            t = True


'''
(base) corybalaton@Corys-MacBook-Pro Oblig % /Users/corybalaton/opt/anaconda3/bin/python "/Users/corybalaton/Documents/UiO/IN1900/Uke 38/Oblig/quadratic_roots_input.py"
input value a: 1
input value b: 0
input value c: -1
The roots are: 1.0 and -1.0
Do you want to calculate the roots of another second degree polynomial? (y/n): y
input value a: 1
input value b: 0
input value c: -4
The roots are: 2.0 and -2.0
Do you want to calculate the roots of another second degree polynomial? (y/n): n
'''
