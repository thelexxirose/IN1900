s = 0
k = 1
M = 3

while k <= M:
    s += 1/(2*k)**2
    k += 1

print(s)

'''
(base) corybalaton@Corys-MacBook-Pro Uke 36 % python3 sum_while.py
0.3402777777777778
'''
