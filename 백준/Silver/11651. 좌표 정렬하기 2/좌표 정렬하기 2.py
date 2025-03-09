r = int(input())
li = []

for _ in range(r):
    x, y = map(int, input().split())
    li.append((x, y))
li.sort(key=lambda x: (x[1], x[0]))

for i in li:
    print(i[0], i[1])
