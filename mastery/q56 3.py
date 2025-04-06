lst = [5,3,2,3,4,5,5,1,2,1,1]
seen = set()
print(set(lst)) # note that this orders things, that's all.
unique_lst = [x for x in lst if not (x in seen or seen.add(x))] # i'm not grasping the seen.add(x) part.
print(unique_lst)
