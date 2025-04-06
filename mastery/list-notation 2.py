# [] is different to list(). [] is a literal, whereas list() is a constructor
# [] is bytecode, list() requires a function call
import timeit
print(timeit.timeit("[]", number=10**6)) # faster
print(timeit.timeit("list()", number=10**6)) # slower
# list() is more versatile and can convert iterables into lists
# [] can only define new lists.
