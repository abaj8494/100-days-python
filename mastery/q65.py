ts = [item for item in mydict.items()]
# the above is probably a little slower than:
ts_fast = list(mydict.items()) # note that [] is different here than to list.
print(ts_fast)
