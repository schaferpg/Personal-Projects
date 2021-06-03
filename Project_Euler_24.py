# https://projecteuler.net/problem=24

from itertools import permutations
l = (list(permutations(range(0, 10))))
arr = []
for a in l:
    res = int("".join(map(str, a)))
    arr.append(res)
arr.sort()
print(arr[999999])
