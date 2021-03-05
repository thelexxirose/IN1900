def min_max(a):
    minimum = a[0]
    maximum = a[0]
    for i in a:
        if i < minimum:
            minimum = i
        if i > maximum:
            maximum = i

    return minimum, maximum


mi, ma = min_max([4, 8, 6, 9, 5, 3, 4])

print(mi)
print(ma)
