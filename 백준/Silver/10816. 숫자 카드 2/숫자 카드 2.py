c = int(input())
card = list(map(int, input().split()))

a = int(input())
answer = list(map(int, input().split()))

dick = {}

for ca in card:
    if ca in dick:
        dick[ca] += 1
    else:
        dick[ca] = 1

for ans in answer:
    if ans not in dick:
        print(0, end=" ")
    else:
        print(dick[ans], end=" ")
