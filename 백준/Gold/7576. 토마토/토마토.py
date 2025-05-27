from collections import deque

m, n = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(n)]
result = []
queue = deque()
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j))  # 익은사과(시작지점)을 미리 큐에 저장해둠

while queue:
    x, y = queue.popleft()  # 큐가 익은사과(시작지점)을 번갈아가며 옮겨감

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))


for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            exit(0)
        result.append(box[i][j])

print(max(result) - 1)
