N, M = map(int, input().split())
card_list = list(map(int, input().split()))
card_len = len(card_list)
sum = 0

for i in range(0, card_len - 2 ):
    for j in range(i+1, card_len - 1):
        for k in range(j+1, card_len):
            if M < card_list[i] + card_list[j] + card_list[k]:
                continue
            else:
                sum = max(sum, card_list[i] + card_list[j] + card_list[k])
print(sum)
