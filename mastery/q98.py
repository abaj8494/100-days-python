def fibonacci(n):
     if n == 0:
         return 0
     if n == 1:
         return 1
     return fibonacci(n-1) + fibonacci(n-2)

def fibo_until(x):
    n=0
    y=[fibonacci(n)]
    while x >= y[n]:
        fib = fibonacci(n)
        if fib > x:
             break
        n+=1
        y.append(fib)
    return y

print(fibo_until(55))
