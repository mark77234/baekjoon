# 위,아래,앞,뒤,양옆
from collections import deque

N, M, H = map(int, input().split())


box = [[list(map(int, input().split())) for _ in range(M)] for _ in range(H)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

queue = deque()


def bfs():

    while queue:
        z, y, x = queue.popleft()

        for i in range(6):

            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
                if box[nz][ny][nx] == 0:
                    box[nz][ny][nx] = box[z][y][x] + 1
                    queue.append((nz, ny, nx))


for a in range(H):
    for b in range(M):
        for c in range(N):
            if box[a][b][c] == 1:
                queue.append((a, b, c))  # a - z, b - y, c -x
bfs()

result = 0
for a in range(H):
    for b in range(M):
        for c in range(N):
            if box[a][b][c] == 0:
                print(-1)
                exit(0)
            result = max(result, box[a][b][c])


print(result - 1)
