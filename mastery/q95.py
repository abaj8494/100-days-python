str_is_dig = lambda s:True if sum(1 for c in s if c.isdigit()) == len(s) else False
print(str_is_dig("123"))
print(str_is_dig("12a"))
# as it turns out, you don't even need the for loop:
print("123456".isdigit())
print("1a23".isdigit())
