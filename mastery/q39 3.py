my_list = [[random.randint(0,n+2) for _ in range(n)] for _ in range(n)]
max_idx_rows_as_list = lambda l: list(map(lambda x: x.index(max(x)), l))
print(my_list)
print(max_idx_rows_as_list(my_list))
