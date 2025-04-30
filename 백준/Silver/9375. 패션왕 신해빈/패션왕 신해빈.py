r = int(input())

for _ in range(r):

    num = int(input())

    set = {}

    cnt = 1

    for _ in range(num):
        wear, kind = input().split()
        if kind in set:
            set[kind].append(wear)
        else:
            set[kind] = [wear]

    for i in set:
        cnt *= len(set[i]) + 1 # 1 -> 해당 옷을 입고 안입고 
    print(cnt - 1) # 옷을 전부 다 벗엇을 경우 빼기
