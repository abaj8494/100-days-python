list_of_t = [(1,2,3,4),(1,2,3),(4,2,1),(1,2,3)]
print(sorted(list_of_t,key=lambda x: (x[1],x[2])))
