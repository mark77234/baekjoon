N, K = map(int, input().split())

li = []
ans = 0
cnt = 0

for _ in range(N):
    li.append(int(input()))

li.sort(reverse=True)
for coin in li:
    if K >= coin:
        cnt += K // coin
        K %= coin
    if K <= 0:
        break
print(cnt)
