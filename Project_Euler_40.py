# Problem 40 Champernowne's constant: https://projecteuler.net/problem=40

b_s = ""
for i in range(1, 200000):
    b_s += str(i)

total = 0
total = int((b_s[0]))
total *= int((b_s[9]))
total *= int((b_s[99]))
total *= int((b_s[999]))
total *= int((b_s[9999]))
total *= int((b_s[99999]))
total *= int((b_s[999999]))

print(total)

