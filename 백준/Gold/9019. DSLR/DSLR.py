from collections import deque

T = int(input())


for _ in range(T):
    A, B = map(int, input().split())
    visited = [False for _ in range(10001)]

    q = deque()
    q.append([A, ""])

    visited[A] = True

    while q:
        val, command = q.popleft()

        if val == B:
            print(command)
            break

        d = val * 2 % 10000

        if not visited[d]:
            visited[d] = True
            q.append([d, command + "D"])

        s = (val - 1) % 10000

        if not visited[s]:
            visited[s] = True
            q.append([s, command + "S"])

        l = val // 1000 + (val % 1000) * 10

        if not visited[l]:
            visited[l] = True
            q.append([l, command + "L"])

        r = val // 10 + (val % 10) * 1000

        if not visited[r]:
            visited[r] = True
            q.append([r, command + "R"])
