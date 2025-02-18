r = int(input())
li = [0 for _ in range(10000 + 1)]

for _ in range(r):
    a = int(input())
    li[a] += 1

for i in range(10001):
    if li[i] > 0:
        for _ in range(li[i]):
            print(i)
