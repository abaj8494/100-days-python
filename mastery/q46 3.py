my_list = list(range(10))
replace_evens = lambda l: list(map(lambda y: y+1 if y%2==0 else y, l))
print(replace_evens(my_list))
