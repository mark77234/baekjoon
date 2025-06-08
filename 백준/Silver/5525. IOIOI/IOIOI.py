n = int(input())
m = int(input())
s = input()

cnt = 0
ans = 0

i = 0
while i < (m - 1):
    tmp = s[i : i + 3]
    if tmp == "IOI":
        i += 2
        cnt += 1

        if cnt == n:
            cnt -= 1  # n = 2인 경우 IOIOI 다음에 IOIOIOI 될 수도 있으니
            ans += 1

    else:
        i += 1
        cnt = 0


print(ans)
