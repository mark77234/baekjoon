a, b = map(int, input().split())

dict = {}
find = []

for _ in range(a):
    arr = input().split()
    dict[arr[0]] = arr[1]

for _ in range(b):
    find = input()
    print(dict[find])
