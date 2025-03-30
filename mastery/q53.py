list_nums = [random.randint(0,5) for _ in range(5)]
def mode(l):
  uniques = set(l)
  mo = (0,) # most often
  for x in uniques:
    y = l.count(x)
    if y > mo[0]:
      mo = (y, x)
  return mo[1]
print(list_nums)
print(mode(list_nums))
