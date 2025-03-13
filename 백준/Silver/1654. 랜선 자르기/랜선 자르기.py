import sys

input = sys.stdin.readline
K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]
start = 1
end = max(lines)

while start <= end:
    num = 0
    mid = (start + end) // 2
    for i in lines:
        num += i // mid

    if num >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)
