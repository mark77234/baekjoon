s = input()
score = list(map(int, input().split()))

high = max(score)
long = len(score)


for i in range(long):
    score[i] = score[i] / high * 100

avg = sum(score) / long
print(avg)
