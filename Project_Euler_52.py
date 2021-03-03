# Problem 52 Permuted multiples: https://projecteuler.net/problem=52

# Find the smallest positive integer, x, such that 2x, 3x, 4x,
# 5x, and 6x, contain the same digits.

def permuted_multiples(num):
    num1 = str(num)
    count = 0
    for i in range(2,7):
        num2 = str(num*i)
        if same_num_checker(num1, num2):
            count += 1
    if count == 5:
        return True
    return False

# Checks to see if the digits in the two numbers are the same
def same_num_checker(num1, num2):
    if len(num1) != len(num2):
        return False
    num1 = list(num1)
    
    for i in range(len(num2)):
        if num2[i] in num1:
            num1.remove(num2[i])
            
        else:
            return False
    return True
        
num = 2
while num < 1000000:
    if permuted_multiples(num):
        print(num)
        break
    num += 1 
