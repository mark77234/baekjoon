r = int(input())

li = []
ans = []
op = []
bool = True

i = 1
while len(ans) < r:
    a = int(input())

    while True:
        if a < i:
            ans.append(li.pop())
            if ans[-1] != a:
                bool = False
            op.append("-")
            break
        li.append(i)
        i += 1
        op.append("+")

if bool == False:
    print("NO")
else:
    for i in op:
        print(i)
