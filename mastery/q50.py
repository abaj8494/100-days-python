threshold_replace = lambda l, t: [ [ t if l[row_idx][col_idx] > t else l[row_idx][col_idx] for col_idx in range(len(row)) ] for row_idx, row in enumerate(l) ]
print(threshold_replace(twod_list, 5))
