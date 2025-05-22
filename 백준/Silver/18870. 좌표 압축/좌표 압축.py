import sys

input = sys.stdin.readline

n = int(input())

X = list(map(int, input().split()))

arr = sorted(set(X))
dict = {}

for i in range(len(arr)):
    dict[arr[i]] = i

for i in X:
    print(dict[i], end=" ")
