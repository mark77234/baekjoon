n = int(input())

li = [0] * (n + 1)

if n == 1:
    print(1)
else:
    li[0] = 1
    li[1] = 1
    for i in range(2, n + 1):
        li[i] = li[i - 1] + 2 * li[i - 2]
    print(li[n] % 10007)
