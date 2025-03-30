nested_list = [[ [ random.randint(0,4) for _ in range(4) ] for _ in range(3) ] for _ in range(2) ]
twod_nested_list = [ [ random.randint(0,4) for _ in range(4) ] for _ in range(3) ]
print(nested_list)
unwrap_2d = lambda l: [x for rows in l for x in rows]
print(unwrap_2d(twod_nested_list))
print(nested_list)
unwrap_3d = lambda l: [x for matrices in l for rows in matrices for x in rows]
print(unwrap_3d(nested_list))
