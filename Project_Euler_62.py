def cubed(num):
    return num ** 3

def sort(num):
    return sorted([i for i in str(num)])

arr = []
for i in range(1,10000):
    arr.append(sort(cubed(i)))

for i in range(1, len(arr)-1):
    count = 0
    num = 0 
    for j in range(i, len(arr)):
        if arr[i] == arr[j]:
            num = i + 1
            count += 1
    if count == 5:
        print(cubed(num))
       
