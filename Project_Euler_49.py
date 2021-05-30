import itertools


def Sieve(n):
    primes = []
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False

    for p in range(n+1):
        if prime[p] and len(str(p)) == 4:
            
            primes.append(p)
    return primes

def checker(arr):
    arr.sort()
    newArr = []
    answer = []
    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)):
            if arr[j]-arr[i] + arr[j] in arr:
                return arr[i], arr[j], 2 * arr[j]-arr[i]
    return None
            
def permutations(primes):
    for p in primes:
        arr = []
        answer = []
        per = itertools.permutations(map(int, str(p)))
        for val in per:
            res = int("".join(map(str,list(val))))
            if res in primes and res not in arr:
                arr.append(res)
            if checker(arr) != None:
                answer.append(checker(arr))
    return answer

print(permutations(Sieve(9999)))
