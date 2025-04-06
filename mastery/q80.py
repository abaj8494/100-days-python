""" returns the highest number that is divisible by both a and b """
def lcm(a, b):
    i = 1
    while True:
        if i%a==0 and i%b==0:
            return i
        else:
            i += 1

print(lcm(8,6))
