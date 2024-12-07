def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))


def fibo(a = 0, b = 1, limit = 20):
    f = [a, b]
    for i in range(limit):
        c = a + b
        f.append(c)
        a = b
        b = c
    print(f)

fibo(limit = 30)