import sys

input = sys.stdin.readline

r = int(input())

li = []
mode = {}
many = []

for i in range(r):
    li.append(int(input()))

li.sort()

print(round(sum(li) / len(li)))
print(li[(len(li) // 2)])

for i in li:
    if i in mode:
        mode[i] += 1
    else:
        mode[i] = 1

high = max(mode.values())

for i in mode:
    if mode[i] == high:
        many.append(i)

if len(many) > 1:
    print(many[1])
else:
    print(many[0])
print(max(li) - min(li))
