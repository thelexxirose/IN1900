s = 0
M = 3

for i in range(M):
    # Error: k is not defined. Solution: define k = i + 1 inside loop,
    # since i starts at 0 and ends at 2
    # and we want k to go from 1 to 3.
    k = i + 1
    # Error: no parenthesis around 2*k
    # This error will give a different answer if not corrected
    # since python will evaluate the equation
    # to be 1/2 * k^2, which is not the correct answer
    # to the equation given in the assignment.
    s += 1/(2*k)**2

print(s)

'''
(base) corybalaton@Corys-MacBook-Pro Uke 36 % python3 sum_for.py
0.3402777777777778
'''
