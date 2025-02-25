from collections import deque

a = int(input())
li = deque([i + 1 for i in range(a)])


while len(li) > 1:
    li.popleft()
    li.append(li[0])
    li.popleft()

print(li[0])
