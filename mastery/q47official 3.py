import random
matrix = [[random.random() for _ in range(3)] for _ in range(3)]
min_col = [min(row[i] for row in matrix) for i in range(3)]
max_col = [max(row[i] for row in matrix) for i in range(3)]
normalized_matrix = [[(row[i] - min_col[i]) / (max_col[i] - min_col[i]) for i in range(3)] for row in matrix]
print(normalized_matrix)
