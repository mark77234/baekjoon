import sys

input = sys.stdin.readline

li = []


def push(val):
    li.append(val)


def pop():
    if not li:
        print(-1)
    else:
        print(li.pop())


def size():
    print(len(li))


def empty():
    print(1 if not li else 0)


def top():
    print(li[-1] if li else -1)


r = int(input().strip())
for _ in range(r):
    ans = input().strip()

    if " " in ans:
        word, val = ans.split()
        val = int(val)
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
    elif word == "top":
        top()
