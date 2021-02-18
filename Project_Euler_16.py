# Power digit Sum Problem 16: https://projecteuler.net/problem=16

digit_total = 0
total = 2 ** 1000
string = str(total)
for t in string:
    digit_total += int(t)
print(digit_total)
