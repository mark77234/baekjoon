N, K = map(int, input().split())
li = []
ans = []
count = K - 1

for i in range(1, N + 1):
    li.append(i)


while True:
    if len(li) < 1:
        break
    if K > len(li):
        while K > len(li):
            K -= len(li)
            if K < len(li):
                break
    ans.append(li.pop(K - 1))
    K += count


formatted = "<" + ", ".join(map(str, ans)) + ">"
print(formatted)
