# 1000 digit Fibonacci number Problem 25: https://projecteuler.net/problem=25
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


num = 1
num2 = 1
total = 0
count = 2
while len(str(total)) != 1000:
    total = num + num2
    num = num2
    num2 = total
    count += 1

print(count)
