my_list = [random.randint(0,n) for _ in range(n)]
check_nonzero = lambda l: all(l)
print(my_list)
print(check_nonzero(my_list))
