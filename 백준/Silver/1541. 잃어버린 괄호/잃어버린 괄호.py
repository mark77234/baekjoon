formular = input().split("-")

li = []
sum = 0

for a in formular:
    nums = a.split("+")
    for a in nums:
        sum += int(a)
    li.append(sum)
    sum = 0

tot = li[0]
for i in range(1, len(li)):
    tot -= li[i]
print(tot)
