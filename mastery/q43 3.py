import math
first_list = [1, 2, 0.5, 0.25]
second_list = list(range(4))
pairwise_euc = lambda x, y: [abs(i[0] - i[1]) for i in zip(x,y)]
print(pairwise_euc(first_list, second_list))
