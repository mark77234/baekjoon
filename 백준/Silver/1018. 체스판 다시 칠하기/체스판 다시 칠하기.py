col, row = map(int, input().split())
arr = []


count = []

for i in range(col):
    arr.append(input())

for s1 in range(col - 7):
    for s2 in range(row - 7):
        w_count = 0
        b_count = 0

        for c in range(s1, s1 + 8):
            for r in range(s2, s2 + 8):
                if (c + r) % 2 == 0:
                    if arr[c][r] != "W":
                        w_count += 1
                    else:
                        b_count += 1
                else:
                    if arr[c][r] != "B":
                        w_count += 1
                    else:
                        b_count += 1

        count.append(w_count)
        count.append(b_count)

print(min(count))
