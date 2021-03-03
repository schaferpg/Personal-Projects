# Problem 26 Reciprocal cycles: https://projecteuler.net/problem=26

# Find the value of d < 1000 for which 1/d contains the longest
# recurring cycle in its decimal fraction part.




def recurring_num(num):
    # 1 % num always is 1 
    mod = 1    
    first_pos = {}
    for i in range(num):
        new_mod = (mod * 10) % num
        if new_mod in first_pos:
            return i - first_pos[new_mod]
        first_pos[new_mod] = i
        mod = new_mod
    return 0

max_cycle_length = 0
max_num = 0
for i in range(1, 1000):
    
    temp_cycle_length = recurring_num(i)
    print(i, temp_cycle_length)
    if temp_cycle_length > max_cycle_length:
        max_num = i
        max_cycle_length = temp_cycle_length
print(max_num)
