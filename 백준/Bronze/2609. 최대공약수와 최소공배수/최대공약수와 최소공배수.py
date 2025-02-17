a, b = map(int, input().split())

div = []

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        div.append(i)

mdiv = max(div)

mmul = (a * b) // mdiv

print(mdiv)
print(mmul)
