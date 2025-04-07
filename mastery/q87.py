import string
sentence = "here are some words in a sentence"
def len_longest_word(s):
    words = s.split()
    return len(max(words, key=len))
    #return ' '.join(["word", "maybe", "cat"])
len_longest_word(sentence)
