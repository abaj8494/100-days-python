lst = [{'name' : 'Alice', 'age': 10}, {'name':'Bob','age':15}, {'name':'Charlie','age':20}]
print(sorted(lst, key=lambda x:x['age']))
