cum_sum = lambda l, axis: [ [sum(l[row_idx][:col_idx+1]) for col_idx in range(len(row)) ] for row_idx, row in enumerate(l) ]
print(twod_list)
print(cum_sum(twod_list, 0))
cum_sum_lambda = lambda l, axis: (
  [
      [sum(col[0:row_idx+1]) for row_idx in range(len(col))]
      for col in zip(*l)
  ] if axis == 0 else [
      [sum(row[0:col_idx+1]) for col_idx in range(len(row))]
      for row in l
  ]
)
print(cum_sum_lambda(twod_list, 0))
print(cum_sum_lambda(twod_list, 1))
