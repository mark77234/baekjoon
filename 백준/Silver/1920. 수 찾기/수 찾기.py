r1 = int(input())
ans = list(map(int, input().split()))
ans.sort()

r2 = int(input())
b = list(map(int, input().split()))

for find in b:
    lt, rt = 0, r1 - 1
    isExist = False
    while lt <= rt:
        mid = (lt + rt) // 2
        if ans[mid] == find:
            isExist = True
            print(1)
            break
        elif ans[mid] < find:
            lt = mid + 1
        else:
            rt = mid - 1
    if not isExist:
        print(0)
