import random
random.seed(3)
n = 10
my_list = [ [random.randint(0,n) for _ in range(n) ] for _ in range(n)]
diag_2d = lambda l: sum(l[i][i] for i in range(n))
print(my_list)
print(diag_2d(my_list))
