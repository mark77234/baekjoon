from collections import deque

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    arr = input()[1:-1].split(",")

    queue = deque(arr)

    flag = 0

    if n == 0:
        queue = []

    for i in p:
        if i == "R":
            flag += 1  # flag는 R의 짝수 여부 R + R = 원래대로
        elif i == "D":
            if len(queue) == 0:
                print("error")  # queue가 비었을 경우 에러
                break
            else:
                if flag % 2 == 0:  # 짝수인 경우 맨 앞에 pop
                    queue.popleft()
                else:
                    queue.pop()  # 아닌경우 맨 뒤 pop
    else:
        if flag % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")
