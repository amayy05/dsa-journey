#factors of number
#difficulty level : easy
#topic= mathematics

#good high o(n)
def factors(n):
    num = n
    result=[]
    for i in range(1,num+1):
        if num % i == 0:
            result.append(i)
    return result


#better o(n/2)
def factors(n):
    num = n
    result = []
    for i in range(1,num // 2):
        if num % i == 0:
            result.append(i)
    result.append(num)
    return result

#best 0(sqrt(n)+0(nlogn))
from math import sqrt
def factors(n):
    result = []
    for i in range(1,int(sqrt(n))+1):
        if n % i == 0:
            result.append(i)
            if n // i != i:
                result.append(num//i)
    result.sort
    return result




