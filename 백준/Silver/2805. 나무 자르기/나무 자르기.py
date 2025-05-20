# import sys

# input = sys.stdin.readline
n, m = map(int, input().split())

trees = list(map(int, input().split()))

start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2
    log = 0
    for tree in trees:
        if mid <= tree:
            log += tree - mid
    if log >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
