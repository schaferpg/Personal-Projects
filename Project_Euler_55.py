def reverse(num):
    num = str(num)
    return int(num[::-1])
def palindrome(num):
    num = str(num)
    for i in range(len(num)//2):
        if num[i] != num[len(num) - i - 1]:
            return "NO"
    return "Yes"


        
lychrel = []
for i in range(1, 10000):
    num = i + reverse(i)
    for j in range(50):
        if palindrome(num) == "Yes":
            break
        num += reverse(num)
    if palindrome(num) == "NO":
        lychrel.append(i)

print(len(lychrel))
