str1, str2 = "listen", "silent"
str3, str4 = "mold", "wolf"
check_anagram = lambda s1,s2: True if sorted(s1)==sorted(s2) else False
print(check_anagram(str1,str2))
print(check_anagram(str3,str4))
