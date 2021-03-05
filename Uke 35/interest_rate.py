# Function that calculates interest depending on parameters P, r, and n
def interest_rate(P, r, n):
    A = P*(1 + r/100)**n
    return A


print(interest_rate(1000, 5, 3))

'''
(base) corybalaton@Corys-MBP Uke 35 % python3 interest_rate.py 
1157.6250000000002
'''
