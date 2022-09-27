N = int(input())

a = 0
while True:
    a_list = list(map(int, str(a)))
    M = a + sum(a_list)
    if M == N:
        print(a)
        break
    if a == N:
        print(0)
        break
    a += 1
