# Problem 29 Distinct Powers: https://projecteuler.net/problem=29

# How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?



def distinct_powers(num):
    arr = []
    for i in range(2, num+1):
        for j in range(2, num+1):
            if i**j not in arr:
                arr.append(i**j)
    return len(arr)

print(distinct_powers(100))
