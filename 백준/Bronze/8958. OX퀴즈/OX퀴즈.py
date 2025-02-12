score = []
multiple = 1
tot = 0

repeat = int(input())

for i in range(repeat):
    answer = input()
    for i in range(len(answer)):
        if answer[i] == "O":
            score.append(1)
        else:
            score.append(0)

    for i in range(len(answer)):
        if (i + 1) == len(answer):
            break
        if answer[i] == "O" and answer[i + 1] == "O":
            multiple += 1
            score[i + 1] = int(score[i + 1] * multiple)
        else:
            multiple = 1

    for i in range(len(score)):
        tot += score[i]

    print(tot)
    tot = 0
    multiple = 1
    score = []
