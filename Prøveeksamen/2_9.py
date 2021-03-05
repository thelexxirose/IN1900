class F:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return self.a*x**2 + self.b*x + self.c


f = F(1.0, 2.0, 0.0)

print(f(2))
