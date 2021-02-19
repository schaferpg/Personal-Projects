# Largest prime factor Problem 3: https://projecteuler.net/problem=3
num = 600851475143     
import math
arr = []

for i in range(1, int(math.sqrt(num))):
    if num % i == 0:
        arr.append(i)

for n in arr:
    for i in range(2, n//2):
        if n % i == 0:
            arr.remove(n)
            break

print(arr[-2])
