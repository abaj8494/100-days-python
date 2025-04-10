ultimate = "frisbee"
non_repeated_char = lambda s: [char for char in s if s.count(char) == 1][0] # you could also use next!
print(non_repeated_char(ultimate))
print(non_repeated_char(ultimate))
