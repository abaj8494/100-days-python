print(twod_nested_list)
transpose = lambda l: [[ l[j][i] for j in range(len(l)) ] for i in range(len(l[0]))]
print(transpose(twod_nested_list))
