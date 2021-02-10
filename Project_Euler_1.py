#Project Euler Problem 1 https://projecteuler.net/problem=1

# Finds the sum of all the multiples of 3 or 5 below 1000

# answer = 233168
three_Sum = five_Sum = 0
# finds the sum of 3 below 1000
for i in range(1000//3+1):
    three_Sum += 3*i
#Finds the sum of 5 below 1000 while checking to make sure duplicates do not
# occur
for i in range(1000//5):
    if (5*i)%3 != 0:
        five_Sum += 5*i

total = three_Sum + five_Sum

print(total)    
