# g/mol
M_c = 12.011
M_h = 1.0079


def alkane_mass(n):
    m = 2*n + 2
    H_total_mass = M_h*m
    C_total_mass = M_c*n
    return f"M(C{n}H{m:2d}) = {(H_total_mass + C_total_mass):3.3f} g/mol)"


for i in range(2, 10):
    print(alkane_mass(i))


'''
(base) corybalaton@Corys-MBP Uke 36 % python3 alkane.py
M(C2H 6) = 30.069 g/mol)
M(C3H 8) = 44.096 g/mol)
M(C4H10) = 58.123 g/mol)
M(C5H12) = 72.150 g/mol)
M(C6H14) = 86.177 g/mol)
M(C7H16) = 100.203 g/mol)
M(C8H18) = 114.230 g/mol)
M(C9H20) = 128.257 g/mol)
'''
