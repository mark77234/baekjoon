a = int(input())
person = []
count = [1 for _ in range(a)]

for _ in range(a):
    key, val = map(int, input().split())
    person.append((key, val))

for i in range(a):
    for j in range(a):
        if person[i][0] < person[j][0] and person[i][1] < person[j][1]:
            count[i] += 1

for k in range(a):
    print(count[k], end=" ")
