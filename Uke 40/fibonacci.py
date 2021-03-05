
def fibonacci(n, a=1, b=1):
    if n == 0 or n == 1:
        return b

    return fibonacci(n-1, b, a+b)


for i in range(16):
    print(f"fibonacci n = {i:>2} <==> {fibonacci(i)}")

'''
(base) corybalaton@Corys-MacBook-Pro Uke 40 % /Users/corybalaton/opt/anaconda3/bin/python "/Users/corybalaton/Documents/UiO/IN1900/Uke 40/fibonacci.py"
fibonacci n =  0 <==> 1
fibonacci n =  1 <==> 1
fibonacci n =  2 <==> 2
fibonacci n =  3 <==> 3
fibonacci n =  4 <==> 5
fibonacci n =  5 <==> 8
fibonacci n =  6 <==> 13
fibonacci n =  7 <==> 21
fibonacci n =  8 <==> 34
fibonacci n =  9 <==> 55
fibonacci n = 10 <==> 89
fibonacci n = 11 <==> 144
fibonacci n = 12 <==> 233
fibonacci n = 13 <==> 377
fibonacci n = 14 <==> 610
fibonacci n = 15 <==> 987
'''
