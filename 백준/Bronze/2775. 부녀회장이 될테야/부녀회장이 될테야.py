r = int(input())
for _ in range(r):
    k = int(input())
    n = int(input())
    lis = [i for i in range(1, n + 1)]

    for i in range(k):
        for j in range(1, n):
            lis[j] += lis[j - 1]
    print(lis[-1])
