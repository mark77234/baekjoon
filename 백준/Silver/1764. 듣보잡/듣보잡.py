N, M = map(int, input().split())

noListen = set()
noFind = set()

for _ in range(N):
    noListen.add(input())

for _ in range(M):
    noFind.add(input())

result = sorted(list(noListen & noFind))

print(len(result))

for i in result:
    print(i)
