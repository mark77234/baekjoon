# DFS 구현
com = int(input())
net = int(input())

graph = [[] for _ in range(com + 1)]

visited = [_ for _ in range(com + 1)]

count = 0

for i in range(net):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)


def DFS(x):
    global count
    count += 1
    visited[x] = True
    for node in graph[x]:
        if visited[node] == True:
            continue
        else:
            DFS(node)


DFS(1)
print(count - 1)
