#Problem 48 Self Powers: https://projecteuler.net/problem=48


n = 1
total = 0
while n != 1000:
    total += n ** n
    n += 1

total = str(total)
print(total[-10:])
