# Pandigital Products Problem 32: https://projecteuler.net/problem=32

# Find the sum of all products whose multiplicand/multiplier/product
# identity can be written as a 1 through 9 pandigital.
import math
def check_pandigital(multiplicand, multiplier, product):
    # Concatanates multiplicand, multiplier, and product. Converts it to a 
    # list sorts the list and compares it with checker(1-9 list)
    checker = [1,2,3,4,5,6,7,8,9]
    total = ""
    total = str(multiplicand) + str(multiplier) + str(product)
    total = list(total)
    total = [int(x) for x in total]
    new_total = sorted(total)
    if new_total == checker:
        return True
    return False


def get_divendends(num):
    
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            if check_pandigital(i, num//i, num):
                return num
    return 0
    

total = 0
num = 2
while num < 10000:
    total += get_divendends(num)
    num += 1

print(total)
