def prod_digits(n):
    digits = len(str(n))
    prod = 1
    for i in range(digits):
        prod *= int(str(n)[i])
    return prod

prod_digits(43)
