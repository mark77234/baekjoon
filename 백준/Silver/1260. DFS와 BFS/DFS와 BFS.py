N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited = [0] * (N + 1)


def dfs(x):
    print(x, end=" ")
    visited[x] = 1

    for i in range(1, N + 1):
        if graph[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)


def bfs(x):
    queue = [x]
    visited[x] = 1
    while queue:
        x = queue.pop(0)
        print(x, end=" ")

        for i in range(1, N + 1):
            if graph[x][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1


dfs(V)
visited = [0] * (N + 1)
print()
bfs(V)
