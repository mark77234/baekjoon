import sys
import heapq

input = sys.stdin.readline

heap = []

r = int(input())

for _ in range(r):
    a = int(input())
    if a != 0:
        heapq.heappush(heap, (abs(a), a))
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
