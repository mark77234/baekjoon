import sys

a, b = map(int, input().split())
input = sys.stdin.readline

pokemon = {}
pokemon_reverse = {}

for i in range(a):
    ans = input().strip()
    pokemon[ans] = i + 1
    pokemon_reverse[i + 1] = ans

for i in range(b):
    find = input().strip()
    if find.isdigit():
        print(pokemon_reverse[int(find)])
    else:
        print(pokemon[find])
