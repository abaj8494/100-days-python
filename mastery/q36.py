import random
n = 3
sort_rows = lambda l: [sorted(row) for row in l]
print(sort_rows([[random.randint(0,n) for _ in range(n)] for _ in range(n)]))
