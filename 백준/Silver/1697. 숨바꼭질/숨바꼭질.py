from collections import deque


n, k = map(int, input().split())

visited = [0] * (10**5 + 1)


def bfs(x):
    visited[x] = 0
    q = deque()
    q.append(x)

    while q:
        cur = q.popleft()
        if cur == k:
            return visited[k]
        for i in (cur - 1, cur + 1, cur * 2):
            if 0 <= i <= 10**5 and not visited[i]:  # 0 -> True 이외 -> False
                visited[i] = visited[cur] + 1
                q.append(i)


print(bfs(n))
