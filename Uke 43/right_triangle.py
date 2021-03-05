from math import sqrt
import matplotlib.pyplot as plt


class RightTriangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = sqrt(a**2 + b**2)
        if self.a < 0 or self.b < 0:
            raise ValueError

    def plot_triangle(self):
        plt.axis("equal")
        plt.plot([0, 0], [0, self.b])
        plt.plot([0, self.a], [0, 0])
        plt.plot([0, self.a], [self.b, 0])
        plt.savefig("right_triangle.png")
        plt.show()


triangle1 = RightTriangle(1, 1)
triangle2 = RightTriangle(3, 4)

print(triangle1.c)
print(triangle2.c)


def test_RightTriangle():
    success = False
    try:
        RightTriangle(1, -1)
    except ValueError:
        success = True
    assert success


test_RightTriangle()

triangle2.plot_triangle()

'''
(base) corybalaton@Corys-MacBook-Pro Uke 43 %
/Users/corybalaton/opt/anaconda3/bin/python
"/Users/corybalaton/Documents/UiO/IN1900/Uke 43/right_triangle.py"

1.4142135623730951
5.0
'''
