a = int(input())
li = []

for _ in range(a):
    key, val = input().split()
    li.append([int(key), val])

li.sort(key=lambda x: x[0])

for i in li:
    print(i[0], i[1])
