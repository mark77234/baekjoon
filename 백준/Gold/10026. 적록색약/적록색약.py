from collections import deque

n = int(input())

color = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
queue = deque()


def bfs(x, y):
    queue.append((x, y))
    visited[x][y] = 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n:
                if color[x][y] == color[nx][ny] and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))


cnt1 = 0
cnt2 = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt1 += 1


for i in range(n):
    for j in range(n):
        if color[i][j] == "R":
            color[i][j] = "G"

visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt2 += 1
print(cnt1, cnt2)
