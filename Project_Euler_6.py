# Sum Square Difference Problme 6: https://projecteuler.net/problem=6


# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.


total_Squared = total_Sum = 0
for i in range(1,101):
    total_Squared += i**2
    total_Sum += i
total_Sum = total_Sum**2
print(total_Sum)
print(total_Squared)
print(-total_Squared + total_Sum)
