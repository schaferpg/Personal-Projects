# Problem 30 Digit fifth powers: https://projecteuler.net/problem=30

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.



def digit_fifth_power(num):
    total = 0
    num = str(num)
    for i in range(len(num)):
        total += int(num[i])**5
    if total == int(num):
        return True
    return False
    
total = 0
num = 2
while num < 2000000:
    if digit_fifth_power(num):
        total += num

    num += 1
    
print(total)

