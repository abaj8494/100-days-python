my_list = [random.randint(0,n) for _ in range(n)]
check_nonzero = lambda l: True if len(list(filter(lambda x: x == 0, l))) == 0 else False
print(my_list)
print(check_nonzero(my_list))
