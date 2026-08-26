#palindrome
#difficulty:easy
#topic : mathematics

def ispalindrome(n):
    if n < 0:
        return False
    original = n
    palindrome_number = 0
    while n > 0:
        ld = n % 10
        palindrome_number = (palindrome_number*10)+ld
        n = n // 10
    return palindrome_number == original

