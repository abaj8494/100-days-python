def gcd(a, b):
    limit = max(a,b)
    highest = 1
    for i in range(1,limit+1):
        if a%i==0 and b%i==0:
            highest=i

    return highest

print(gcd(8,6))
