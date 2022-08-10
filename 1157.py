S = input().lower()
max = loc = 0
for i in range(97, 123):
    a = S.count(chr(i))
    if max < a:
        max = a
        loc = i
    elif max == a:
        loc = 0
if loc > 0:
    print(chr(loc).upper())
else:
    print("?")
