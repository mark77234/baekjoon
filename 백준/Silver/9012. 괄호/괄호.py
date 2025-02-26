r = int(input())
li = []

for _ in range(r):
    li.append(input())

for i in range(r):
    left = 0
    right = 0
    no = 0
    for k in range(len(li[i])):
        if li[i][k] == "(":
            left += 1
        else:
            right += 1
            if right > left:
                no += 1
    if left > right:
        no += 1
    if no > 0:
        print("NO")
    else:
        print("YES")
