# Amicable Numbers Problem 21: https://projecteuler.net/problem=21
import math
    
arr = []

def get_divisors(num):
    arr = []
    for i in range(1, int(math.sqrt(num))):
        if num % i == 0:
            arr.append(i)
            arr.append(num//i)
    return sum(arr) - num


def ambicable_Num(num1, num2):
    if get_divisors(num1) == num2 and get_divisors(num2) == num1 and num1 != num2:
        return True
    
total = 0
num = 5
while num < 10000:
    if ambicable_Num(num, get_divisors(num)) == True:
        total += num
    num += 1

print(total)
