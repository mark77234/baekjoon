r = int(input())
li = []

for i in range(r):
    a, b = map(int, input().split())
    li.append([a, b])
li.sort(key=lambda x: (x[0], x[1]))

for i in li:
    print(i[0], i[1])
