n = int(input())

a = list(map(int, input().split()))

count = [0 for i in range(n)]

minor = 0

for j in range(n):
    if a[j] == 1:
        count[j] += 1
    for i in range(2, a[j]):
        if a[j] % i == 0:
            count[j] += 1

for i in range(n):
    if count[i] == 0:
        minor += 1
print(minor)
