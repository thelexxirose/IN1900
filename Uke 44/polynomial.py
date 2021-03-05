class Quadratic:
    def __init__(self, coefficients):
        # if len(coefficients) != 3:
        #    raise Exception("The list has to contain 3 coefficients")

        self.c = coefficients

    def __call__(self, x):
        ans = 0
        for idx, i in enumerate(self.c):
            ans += i*x**(len(self.c)-1-idx)
        return ans

    def __str__(self):
        ans = ""
        for idx, i in enumerate(self.c):
            if i < 0:
                if (len(self.c)-1-idx) == 1:
                    ans += f"- {abs(i)}*x "
                elif (len(self.c)-1-idx) > 0:
                    ans += f"- {abs(i)}*x**{(len(self.c)-1-idx)} "
                else:
                    ans += f"- {abs(i)}"
            elif i == 0:
                pass
            else:
                if (len(self.c)-1-idx) == 1:
                    ans += f"+ {abs(i)}*x "
                elif (len(self.c)-1-idx) > 0:
                    ans += f"+ {abs(i)}*x**{(len(self.c)-1-idx)} "
                else:
                    ans += f"+ {abs(i)}"
        return ans[2:]


class Cubic(Quadratic):

    def derivative(self):
        return Quadratic([self.c[0]*3, self.c[1]*2, self.c[2]])


quad = Quadratic([1, 3, 2])
print(quad)
print(f"x = 1: {quad(1)} \nx = 2: {quad(2)}")

print("\n")

cube = Cubic([1, 3, 2, 4])
print(cube)
print(f"x = 1: {cube(1)} \nx = 2: {cube(2)}")
print(cube.derivative())

'''
(base) corybalaton@Corys-MacBook-Pro Uke 44 % /Users/corybalaton/opt/anaconda3/bin/python "/Users/corybalaton/Documents/UiO/IN1900/Uke 44/polynomial.py"
1*x**2 + 3*x + 2
x = 1: 6 
x = 2: 12


1*x**3 + 3*x**2 + 2*x + 4
x = 1: 10 
x = 2: 28
3*x**2 + 6*x + 2
'''
