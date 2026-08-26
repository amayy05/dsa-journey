#count digits
#difficulty: easy
#topic : mathematics
#using while loop

def count_digits(n):
    cnt = 0
    while n > 0:
        cnt += 1
        n //= 10
    return cnt

#using log10
from math import log10
def cnt_digit(n):
    return int(log10(n) + 1)

