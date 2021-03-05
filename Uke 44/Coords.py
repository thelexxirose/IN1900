from math import sqrt


class Coords:
    def __init__(self, x, y, z):
        self.coords = [x, y, z]

    def __str__(self):
        return f"({self.coords[0]:.2f}, {self.coords[1]:.2f}, {self.coords[2]:.2f})"

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        return f"{sqrt(self.coords[0]**2 + self.coords[1]**2 + self.coords[2]**2):.2f}"

    def __add__(self, other):
        addition = [self.coords[0] + other.coords[0], self.coords[1] +
                    other.coords[1], self.coords[2] + other.coords[2]]
        return Coords(addition[0], addition[1], addition[2])

    def __sub__(self, other):
        subtraction = [self.coords[0] - other.coords[0], self.coords[1] -
                       other.coords[1], self.coords[2] - other.coords[2]]
        return Coords(subtraction[0], subtraction[1], subtraction[2])


sqrt3 = sqrt(3)
close = Coords(1/sqrt3, 1/sqrt3, 1/sqrt3)
far = Coords(3/sqrt3, 15/sqrt3, 21/sqrt3)
print(close)
print(far)

print("\n")

print(f"The class represents coordinates in {len(close)} dimensions")
print(f"The distance from the centre to the point close is {abs(close)}")
print(f"The distance from the centre to the point far is {abs(far)}")

print("\n")

further = close + far
print(f"The coordinates further are at {further}")
distance = abs(far - close)
print(f"The distance from far to close is {distance}")
centre = further - further
print(f"The coordinates at the centre are {centre}")

'''
(base) corybalaton@Corys-MacBook-Pro Uke 44 % /Users/corybalaton/opt/anaconda3/bin/python "/Users/corybalaton/Documents/UiO/IN1900/Uke 44/Coords.py"
(0.58, 0.58, 0.58)
(1.73, 8.66, 12.12)


The class represents coordinates in 3 dimensions
The distance from the centre to the point close is 1.00
The distance from the centre to the point far is 15.00


The coordinates further are at (2.31, 9.24, 12.70)
The distance from far to close is 14.14
The coordinates at the centre are (0.00, 0.00, 0.00)
'''
