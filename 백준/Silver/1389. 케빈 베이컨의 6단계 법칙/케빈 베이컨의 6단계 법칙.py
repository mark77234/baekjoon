from collections import deque

n, m = map(int, input().split())

friends = [[] for _ in range(n + 1)]


for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)


def bfs(start_node, friends):
    num = [0] * (n + 1)
    visited = [start_node]  # 방문한 숫자를 추가하는 방식
    queue = deque()
    queue.append(start_node)

    while queue:
        start = queue.popleft()
        for node in friends[start]:
            if node not in visited:
                num[node] = num[start] + 1
                queue.append(node)
                visited.append(node)
    return sum(num)


tot = []
for i in range(n + 1):
    tmp = bfs(i, friends)
    if tmp == 0:
        continue
    tot.append(tmp)

print(tot.index(min(tot)) + 1)
