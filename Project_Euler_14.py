# Longest Collatz sequence Problem 14: https://projecteuler.net/problem=14

num = 1
count = 0
big_count = 0
big_num = 0
while num < 1000000:
    
    temp_num = num
    while temp_num != 1:
                
        if temp_num % 2 == 0:
            temp_num = temp_num//2
            count += 1
            
        elif temp_num % 2 != 0:
            temp_num = temp_num*3 + 1
            count += 1

    if count > big_count:
            big_count = count
            big_num = num
    count = 0
    num += 1

print(big_num)
