print(s)
count_chars = lambda s: {char: s.count(char) for char in set(s)}
print(sorted(list(count_chars(s).items()), key=lambda x:x[1]))
