lst = [{'name': 'Vivek', 'age': 25}, {'name': 'Esther', 'age': 22}, {'name': ' Neassa', 'age': 28}]                            
filtered_lst = [x for x in lst if x['age'] > 23]
print(filtered_lst)
