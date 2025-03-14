import sys

input = sys.stdin.readline

r = int(input())

S = set()

for _ in range(r):
    ans = input().split()
    if len(ans) > 1:
        word = ans[0]
        val = int(ans[1])
    else:
        word = ans
        val = 0

    if ans[0] == "add":
        S.add(val)
    elif ans[0] == "remove":
        S.discard(val)
    elif ans[0] == "check":
        if val in S:
            print(1)
        else:
            print(0)
    elif ans[0] == "toggle":
        if val in S:
            S.remove(val)
        else:
            S.add(val)
    elif ans[0] == "all":
        S = set(range(1, 21))
    elif ans[0] == "empty":
        S = set()
