import sys

a = int(input())
li = []

for i in range(a):
    li.append(int(sys.stdin.readline()))
li.sort()

for i in range(a):
    print(li[i])
