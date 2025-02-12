alphabet = list("abcdefghijklmnopqrstuvwxyz")
include = [-1 for i in range(len(alphabet))]

word = input()

for i in range(len(word)):
    for j in range(len(alphabet)):
        if word[i] == alphabet[j]:
            if include[j] != -1:
                break
            include[j] = i

for i in range(len(include)):
    print(include[i], end=" ")
