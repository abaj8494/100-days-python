def percentile(data, percentile):
  data = sorted(data)
  k = (len(data) - 1) * (percentile / 100)
  return data[int(k)]

lst = [10, 20, 30, 40, 50]
q1 = percentile(lst, 25)
q3 = percentile(lst, 75)
lst = [0 if q1 <= x <= q3 else x for x in lst]
print(lst)

lst = [10, 20, 30, 40, 50]
percentile_25th = sorted(lst)[int(len(lst) * 0.25)] # indexing into the first quarter
percentile_75th = sorted(lst)[int(len(lst) * 0.75)]
lst = [0 if percentile_25th <= x <= percentile_75th else x for x in lst]
print(lst)
