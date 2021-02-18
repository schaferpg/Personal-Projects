# Factorial digit sum Problem 20: https://projecteuler.net/problem=20

import math

total_digit = 0 
total = math.factorial(100)

digit_total = str(total)

for d in digit_total:
    total_digit += int(d)

print(total_digit)
