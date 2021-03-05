def f(x, y):
    def func_1(x, y): return 4*x**3*y - 2*x*y
    def func_2(x, y): return 4*x**3*y + 2*x*y

    l = []
    for i in y:
        if i <= 0:
            l.append(func_1(x, y))
        else:
            l.append(func_2(x, y))

    return l
