sugar = int(input())

cnt = 0

if sugar % 5 == 0:
    print(sugar // 5)
else:
    while sugar > 0:
        cnt += 1
        sugar -= 3
        if sugar % 5 == 0:
            print(cnt + (sugar // 5))
            break
        elif 0 < sugar < 3:
            print(-1)
            break
        elif sugar == 0:
            print(cnt)
            break
