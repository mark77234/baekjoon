def alpha_to_num(alphabet):
    return ord(alphabet) - 96


L = int(input())
alpha = input()

hash = 0
for i in range(L):
    hash += alpha_to_num(alpha[i]) * 31**i

print(hash)
