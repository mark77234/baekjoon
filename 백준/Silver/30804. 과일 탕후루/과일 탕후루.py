n = int(input())
fruit = list(map(int, input().split()))

kind = 0
cnt = {}
left = 0
ans = 0


for right in range(n):
    if fruit[right] not in cnt:
        cnt[fruit[right]] = 1
        kind += 1
    else:
        cnt[fruit[right]] += 1

    while len(cnt) > 2:
        cnt[fruit[left]] -= 1
        if cnt[fruit[left]] == 0:
            del cnt[fruit[left]]
        left += 1
    ans = max(ans, right - left + 1)

print(ans)
