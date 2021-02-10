# Project Euler Problem 2: https://projecteuler.net/problem=2

# By considering the terms in the Fibonacci sequence whose values do
# not exceed four million, find the sum of the even-valued terms.

even_Total = 0
total = 0
x = 0
y = 1
while total < 4000000:
    total = x + y
    if total % 2 == 0:
        even_Total += total
    x = y
    y = total
    
print(even_Total)
