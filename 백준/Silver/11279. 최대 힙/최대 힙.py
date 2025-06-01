import heapq
import sys

input = sys.stdin.readline

r = int(input())

heap = []

for _ in range(r):
    n = int(input())
    if n == 0:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -n)
