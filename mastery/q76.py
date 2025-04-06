def factorial(n):
  if n < 0:
    return -1
  if n == 0:
    return 1
  return n*factorial(n-1)

print(factorial(-1))
print(factorial(10))

def fibonacci(n):
     if n == 0:
         return 0
     if n == 1:
         return 1
     return fibonacci(n-1) + fibonacci(n-2)
for i in range(10):
     print(fibonacci(i))
