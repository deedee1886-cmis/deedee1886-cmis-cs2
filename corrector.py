def function1(x, n):
    if n <= 0:
        return x
    else:
        return 1 + function1(x, n - 1)

def function2(a, b):
    if a <= 0:
        return 1 + function1(a+1, b**a)
    else:
        return b

def function3(a, b):
    if b <= 0:
        return a
    else:
        return a + b + function3(a, b -1)

def function4(a, b, c):
    if a > b and a > c:
        return 1 + function4(b+1, c, a)
    elif b > a or b > c:
        return 1 - function4(b-1, c, a)
    else:
        return a+b+c
