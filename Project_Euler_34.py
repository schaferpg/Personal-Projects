# Problem 34 Digit Factorials: https://projecteuler.net/problem=34

# Find the sum of all numbers which are equal to the sum of the
# factorial of their digits.

import math


def curious_number(num):
    num = str(num)
    total = 0
    for i in range(len(num)):
        total += math.factorial(int(num[i]))
    if total == int(num):
        return True
    return False


num = 3
total = 0
while num < 700000:
    if curious_number(num):
        total += num

    num += 1
print(total)
