count, sum = map(int, input().split())

card = list(map(int, input().split()))
result = 0

for i in range(count):
    for j in range(i + 1, count):
        for k in range(j + 1, count):
            if card[i] + card[j] + card[k] <= sum:
                result = max(result, card[i] + card[j] + card[k])

print(result)
