from collections import deque

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
comunity = 0
people = []

def BFS(x, y):
    global comunity
    cnt = 1  # 시작 지점의 집을 포함
    q = deque()
    q.append((x, y))
    visited[x][y] = comunity
    graph[x][y] = 0  # 방문한 집은 0으로 변경

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    visited[nx][ny] = comunity
                    q.append((nx, ny))
                    cnt += 1
    people.append(cnt)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            comunity += 1
            BFS(i, j)

print(comunity)
people.sort()
for count in people:
    print(count)