import sys

input = sys.stdin.readline
n = int(input())

dp = [0, 1]

for i in range(2, n + 1):
    low = 4
    j = 1
    while i >= j**2:
        low = min(low, dp[i - (j**2)])
        j += 1
    dp.append(low + 1)
print(dp[n])
