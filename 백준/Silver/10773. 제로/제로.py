li = []

r = int(input())

for i in range(r):
    val = int(input())
    if val == 0:
        li.pop()
    else:
        li.append(val)

print(sum(li))
