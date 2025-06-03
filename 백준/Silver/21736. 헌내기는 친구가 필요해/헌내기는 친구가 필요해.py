from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

campus = []
visited = [[0] * m for _ in range(n)]


for _ in range(n):
    campus.append(list(map(str, input().strip())))

queue = deque()

for i in range(n):
    for j in range(m):
        if campus[i][j] == "I":
            queue.append([i, j])
            visited[i][j] = 1


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            if campus[nx][ny] == "X":
                continue
            visited[nx][ny] = 1
            if campus[nx][ny] == "P":
                cnt += 1
            queue.append([nx, ny])


if cnt == 0:
    print("TT")
else:
    print(cnt)
