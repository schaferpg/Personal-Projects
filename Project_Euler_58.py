# https://projecteuler.net/problem=58

import time
startTime = time.time()

def isPrime(num):
    d = 3
    while d * d <= num:
        if num % d == 0:
            return False
        d += 2
    return True

i = 3
total_corners = 5
top_right_count = 6
prime_count = 0
percentage = 100

while percentage > .1:
    bottom_right = i ** 2
    bottom_left = bottom_right - i + 1
    top_left = bottom_right - total_corners + 1
    top_right = bottom_right - top_right_count
    if isPrime(bottom_left):
        prime_count += 1
    if isPrime(top_left):
        prime_count += 1
    if isPrime(top_right):
        prime_count += 1
    percentage = prime_count / total_corners
    i += 2
    top_right_count += 6
    total_corners += 4

print(i-2)
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
