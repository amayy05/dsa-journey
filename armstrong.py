#armstrong number
# difficulty easy
# topic : mathematics

def armstrong(n):
    k = len(str(n))
    armstrong_number = 0
    num = n
    while num > 0:
        ld = num % 10
        armstrong_number = armstrong_number + (ld ** k)
        num = num // 10
    return armstrong_number == n


