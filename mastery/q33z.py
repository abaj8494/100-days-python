mean_cols = lambda l: [sum(l[i]) / len(l) for i in range(len(l))]
n = 5
d2_list = [[random.randint(0,10) for _ in range(n)] for _ in range(n)]
print(mean_cols(d2_list))
