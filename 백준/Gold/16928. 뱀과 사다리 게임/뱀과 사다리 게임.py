from collections import deque

DOWN, UP = map(int, input().split())

board = [0] * 101
visited = [False] * 101

ladder = {}
snake = {}

for _ in range(DOWN):
    start, end = map(int, input().split())
    ladder[start] = end

for _ in range(UP):
    start, end = map(int, input().split())
    snake[start] = end


def game(start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        current = q.popleft()
        for i in range(1, 7):
            next = current + i
            if 0 <= next <= 100 and visited[next] == False:
                if next in ladder:
                    next = ladder[next]

                if next in snake:
                    next = snake[next]

                if visited[next] == False:
                    q.append(next)
                    visited[next] = True
                    board[next] = board[current] + 1


game(1)
print(board[100])
