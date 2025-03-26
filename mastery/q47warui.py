random.seed(4)
twod_list = [list(random.randint(0,10) for _ in range(10)) for _ in range(4)]
get_range_rows = lambda l: sorted(new_list,reverse=True)[0] - sorted(new_list)[0]
normalise_2d_rows = lambda l: [ [l[row_idx][col_idx]/get_range_rows(row) for col_idx in range(len(row))] for row_idx, row in enumerate(l) ]
get_range_cols = lambda matrix: (num_rows := len(matrix),
				 num_cols := len(matrix[0]),
				 [max(row[col_idx] for row in matrix) - min(row[col_idx] for row in matrix) for col_idx in range(num_cols)])[-1]
normalise_2d_cols = lambda l: [ [(l[row_idx][col_idx]-min(row[col_idx] for row in l))/(get_range_cols(l))[col_idx] for col_idx in range(len(row))] for row_idx, row in enumerate(l) ]

print(twod_list)
print(get_range_cols(twod_list))
#print(sorted(twod_list,reverse=True))
#print(normalise_2d_rows(twod_list))
print(normalise_2d_cols(twod_list))
