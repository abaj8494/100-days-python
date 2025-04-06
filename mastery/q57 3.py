lst1 = [5,2,5,3,1,2]
lst2 = [1,3,9,5,2]
print(set(lst1).intersection(lst2))
# turns out there's another way:
print(set(lst1) & set(lst2))
