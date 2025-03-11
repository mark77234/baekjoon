import sys

input = sys.stdin.readline


def rounds(num):  # 사사오입 round -> 오사오입
    return int(num) + (1 if num - int(num) >= 0.5 else 0)


r = int(input())

if r == 0:
    print(0)
else:
    avg = rounds((r * 0.3) / 2)

    li = []

    for _ in range(r):
        num = int(input())
        li.append(num)

    li.sort()

    res = li[avg : r - avg]

    print(rounds(sum(res) / len(res)))
