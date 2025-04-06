lstrings = ["hello", "world", "worldly", "hells"]

def longest_prefix(lstr):
      if not lstr:
          return ""
      shortest_str = min(lstr, key=len)
      longest_common_prefix = ""
      for i in range(len(shortest_str)):
          current_char = shortest_str[i]
          if all(x[i] == current_char for x in lstr):
              longest_common_prefix += current_char
          else:
              break
      return longest_common_prefix

print(longest_prefix(["flower","flow","flight"]))
