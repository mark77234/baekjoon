from collections import deque

n, m = map(int, input().split())
graph = [[0] * m for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start = (i, j)
        elif graph[i][j] == 0:
            visited[i][j] = 0


def BFS(visited, graph, start):  # 최단거리니 BFS
    queue = deque()
    queue.append(start)
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    visited[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:  # n - 행, m - 열
                if visited[nx][ny] == -1 and graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))


BFS(visited, graph, start)

for i in range(n):
    for j in range(m):
        print(visited[i][j], end=" ")
    print()
