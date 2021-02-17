# Problem 13 Highly Divisible Triangular number: https://projecteuler.net/problem=12

import math


def find_triangular():
    total = 1
    x = 2
    while find_divisor(total) < 500:
        total += x
        x += 1
    return total
"""
Tried using recusion but recurion ends after a while
    total = 0
    for i in range(num + 1):
        total += (i)
    print(total)
    if find_divisor(total) >= 500:
        return total
    else:
        return find_triangular(num+1)
"""

def find_divisor(total):
    count = 0
    for i in range(1, int(math.ceil(math.sqrt(total)))):
        if total % i == 0:
            count += 2
    return count
    
print(find_triangular())
