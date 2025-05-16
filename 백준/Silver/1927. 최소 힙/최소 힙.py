import heapq
import sys

input = sys.stdin.readline

r = int(input())

heap = []

for i in range(r):
    a = int(input())
    if a < 1:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, a)
