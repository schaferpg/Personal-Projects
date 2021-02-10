# Project Euler Problme 4: https://projecteuler.net/problem=4


# Find the largest palindrome made from the product of two 3-digit numbers.



def palindrome(num):
    for i in range(len(num)//2):
        if num[i] == num[-i-1]:
            continue
        else:
            return False
    return True

    
holder = []
def multiplier():
    for i in range(100,999):
        for j in range(100,999):
            if palindrome(str(j*i)) == True:
                holder.append(j*i)
    

multiplier()

max_num = 0
for h in holder:
    if h > max_num:
        max_num = h

print(max_num)
