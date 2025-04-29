r = int(input())


for _ in range(r):
    num = int(input())
    li = [0] * (num + 1)

    if num == 1:
        print(1)
    elif num == 2:
        print(2)
    elif num == 3:
        print(4)
    else:
        li[1] = 1
        li[2] = 2
        li[3] = 4
        for i in range(4, num + 1):
            li[i] = li[i - 1] + li[i - 2] + li[i - 3]
        print(li[num])
