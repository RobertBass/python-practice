def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))


# FIBONACCI CON ITERACIONES
def fibo(limit = 10):
    f = []
    for i in range(limit+1):
        if len(f) < 2:
            f.append(i)
        else:
            f.append(f[i-1] + f[i-2])
    print(f)


# FIBONACCI RECURSIVO
f2 = []
def fiboRec(c = 0, n = 0, limit = 10):
    if c <= limit:
        if len(f2) < 2:
            f2.append(n)
            n += 1
            c += 1
            fiboRec(c, n)
        else:
            f2.append(f2[c-2] + f2[c-1])
            c += 1
            fiboRec(c)

    
fibo()
fiboRec()
print(f2)