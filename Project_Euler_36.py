# Double-base palindromes Problem 36: https://projecteuler.net/problem=36

# Find the sum of all numbers, less than one million, which are
# palindromic in base 10 and base 2.




def palindrome(num):
    num = str(num)
    for i in range(len(num)//2):
        if num[i] != num[-i-1]:
            return False
    return True

def binary_palindrome(num):
    num = str(num)
    num = num[2:len(num)]
    return palindrome(num)


def check_double_palindrome(num):
    if palindrome(num) and binary_palindrome(bin(num)):
        return True
total = 0
num = 1
while num < 1000000:

    if check_double_palindrome(num):
        total += num

    num += 1

print(total)
