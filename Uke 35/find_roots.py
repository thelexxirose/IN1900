from math import pi


def find_roots(a, b, c):
    eval_sroot = (b**2 - (4*a*c))**(1/2)

    roots = {
        "x_1": (-b + eval_sroot)/(2*a),
        "x_2": (-b - eval_sroot)/(2*a)
    }

    return roots


eval_roots = find_roots(81*pi, 1800, -6165)

print(f"""
    First x value  = {eval_roots["x_1"]:.2f} 
    Second x value = {eval_roots["x_2"]:.2f}
    """)

'''
(base) corybalaton@Corys-MBP Uke 35 % python3 find_roots.py 

    First x value  = 0.50 
    Second x value = 0.33
    
'''
