n = int(input())
con = []

for i in range(1, n + 1):
    if sum(map(int, str(i))) + i == n:
        con.append(i)

if len(con) == 0:
    print(0)
else:
    print(min(con))
