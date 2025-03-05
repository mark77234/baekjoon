import sys

input = sys.stdin.readline

li = []


def push(val):
    li.append(val)


def pop():
    if not li:
        print(-1)
    else:
        print(li.pop(0))


def size():
    print(len(li))


def empty():
    if not li:
        print(1)
    else:
        print(0)


def front():
    if not li:
        print(-1)
    else:
        print(li[0])


def back():
    if not li:
        print(-1)
    else:
        print(li[-1])


r = int(input())

for _ in range(r):
    ans = input().strip()
    if " " in ans:
        ans = ans.split(" ")
        word = ans[0]
        val = int(ans[1])
    else:
        word = ans
        val = 0

    if word == "push":
        push(val)
    elif word == "pop":
        pop()
    elif word == "size":
        size()
    elif word == "empty":
        empty()
    elif word == "front":
        front()
    elif word == "back":
        back()
