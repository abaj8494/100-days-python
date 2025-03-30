import random
random.seed()
list_nums = [random.randint(0,5) for _ in range(5)]
median = lambda l: l[len(l) / 2 if len(l) % 2 == 0 else len(l)//2 ]
print(list_nums)
print(median(list_nums))








