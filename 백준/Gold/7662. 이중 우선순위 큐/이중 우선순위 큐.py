import sys
import heapq

input = sys.stdin.readline


def isEmpty(nums):
    for i in nums:
        if i[1] > 0:
            return False
    return True


T = int(input())
for _ in range(T):

    nums = dict()
    max_heap = []
    min_heap = []

    k = int(input())
    for _ in range(k):
        command, val = input().split()
        num = int(val)
        if command == "I":
            if num in nums:
                nums[num] += 1

            else:
                nums[num] = 1
                heapq.heappush(max_heap, -num)
                heapq.heappush(min_heap, num)

        elif command == "D":
            if not isEmpty(nums.items()):
                if num == 1:
                    while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
                        temp = -heapq.heappop(max_heap)
                        if temp in nums:
                            del nums[temp]
                    nums[-max_heap[0]] -= 1
                else:
                    while min_heap[0] not in nums or nums[min_heap[0]] < 1:
                        temp = heapq.heappop(min_heap)
                        if temp in nums:
                            del nums[temp]
                    nums[min_heap[0]] -= 1

    if isEmpty(nums.items()):
        print("EMPTY")
    else:
        while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
            heapq.heappop(max_heap)
        while min_heap[0] not in nums or nums[min_heap[0]] < 1:
            heapq.heappop(min_heap)
        print(-max_heap[0], min_heap[0])
