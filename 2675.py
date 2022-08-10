a = int(input())
for b in range(a):
    R, P = list(input().split())
    for c in P:
        print(int(R)*c, end='')
    print()
