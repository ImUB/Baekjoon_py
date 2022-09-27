def isprime(a) :
    if a == 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return a

M = int(input())
N = int(input())
lst = list(range(M, N+1))
n_lst = []
for i in lst:
    if isprime(i) != None:
        if isprime(i) == False:
            pass
        else:
            n_lst.append(isprime(i))
if len(n_lst) > 0:
    print(sum(n_lst))
    print(min(n_lst))
else:
    print(-1)
