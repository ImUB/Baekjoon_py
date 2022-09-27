def isprime(a) :
    if a == 1:
        return 0
    for i in range(2, a):
        if a % i == 0:
            return 0
    return 1

N = int(input())
Numbers = map(int, input().split())
count = 0
for i in Numbers:
    if isprime(i) != None:
        count += isprime(i)
print(count)
