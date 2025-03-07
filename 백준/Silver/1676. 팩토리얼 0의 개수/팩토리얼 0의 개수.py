a = int(input())
fact = 1
cnt = 0

for i in range(1, a + 1):
    fact *= i

while True:
    if fact % 10 == 0:
        cnt += 1
        fact //= 10
    else:
        break
print(cnt)
