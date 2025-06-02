import sys

input = sys.stdin.readline
n, m, b = map(int, input().split())

ground = []

ans = int(1e9)
tmp = 0

for _ in range(n):
    ground.append(list(map(int, input().split())))

for r in range(257):
    erase = 0
    put = 0

    for i in range(n):
        for j in range(m):
            if ground[i][j] > r:
                erase += ground[i][j] - r
            else:
                put += r - ground[i][j]

    if put > erase + b:
        continue

    tmp = erase * 2 + put
    if tmp <= ans:
        ans = tmp
        level = r

print(ans, level)
