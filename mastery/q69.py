import string
remove_punc = lambda s: s.translate(str.maketrans('','',string.punctuation))
print(remove_punc("remove, punc? punk!"))
