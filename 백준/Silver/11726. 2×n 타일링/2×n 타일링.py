n = int(input())

li = [0] * (n + 1)

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    li[1] = 1
    li[2] = 2
    for i in range(3, n + 1):
        li[i] = li[i - 1] + li[i - 2]
    print(li[n] % 10007)
