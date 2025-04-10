vowel_counter= lambda s: sum(1 for c in s.lower() if c in "aeiou")
print(vowel_counter("hello world's people"))
