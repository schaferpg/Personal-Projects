def isPrime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    d = 3
    while d ** 2 <= num:
        if num % d == 0:
            return False
        d += 2
    return True



def rotations(num):
    num = str(num)
    for i in range(len(num)):
        if i == 0:
            new_num = num[i:len(num)]
        else:
            new_num = num[i:len(num)] + num[:i]
        if isPrime(int(new_num)) == False:
            return False
    return True


i = 2
count = 0
while i < 1000000:
    if rotations(i) == True:
        count += 1
    i += 1
print(count)

