li = []

r = int(input())

for _ in range(r):
    a = int(input())
    for i in range(a + 1):
        if i == 0:
            li.append([1, 0])
        elif i == 1:
            li.append([0, 1])
        else:
            li.append([li[i - 1][0] + li[i - 2][0], li[i - 1][1] + li[i - 2][1]])

    print(li[-1][0], li[-1][1])
    li.clear()
