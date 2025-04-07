num = 804
def sum_digits(n):
    digits = len(str(n))
    sum = 0
    for i in range(digits):
        sum += int(str(n)[i])
    return sum

sum_digits(num)
