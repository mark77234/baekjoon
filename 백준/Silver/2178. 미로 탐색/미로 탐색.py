from collections import deque

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))


def BFS(x, y):
    q = deque()
    q.append((x, y))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    continue
                if graph[nx][ny] == 1:  # 1이면 방문 (따로 방문처리 안해도됨)
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))


BFS(0, 0)
print(graph[n - 1][m - 1])
