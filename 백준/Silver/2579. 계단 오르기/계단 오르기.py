r = int(input())

stairs = [0] * (r + 1)

for i in range(1, r + 1):
    stairs[i] = int(input())

dp = [0] * (r + 1)

if r < 2:
    dp[1] = stairs[1]
else:
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    for i in range(3, r + 1):
        dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

print(dp[r])
