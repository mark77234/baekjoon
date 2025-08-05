N, M = map(int, input().split())  # N - 세로 , M - 가로

arr = [list(map(int, input().split())) for _ in range(N)]

tetris = [
    [(0, 1), (0, 2), (0, 3)],
    [(1, 0), (2, 0), (3, 0)],  # 1x4 형태
    [(0, 1), (1, 0), (1, 1)],  # 2x2형태
    [(1, 0), (1, 1), (2, 1)],
    [(0, -1), (1, -1), (1, -2)],  # ㄹ자 (회전)
    [(1, 0), (1, -1), (2, -1)],
    [(0, 1), (1, 1), (1, 2)],  # ㄹ자 (대칭)
    [(1, 0), (2, 0), (2, 1)],
    [(0, 1), (0, 2), (1, 0)],  # ㄴ자 (회전)
    [(0, 1), (1, 1), (2, 1)],
    [(0, 1), (0, 2), (-1, 2)],
    [(1, 0), (2, 0), (2, -1)],
    [(0, 1), (0, 2), (1, 2)],  # ㄴ자 (대칭)
    [(1, 0), (2, 0), (0, 1)],
    [(1, 0), (1, 1), (1, 2)],
    [(1, 0), (1, 1), (1, -1)],
    [(1, 0), (1, 1), (2, 0)],  # ㅗ자(회전)
    [(0, -1), (1, 0), (0, 1)],
    [(0, 1), (-1, 1), (1, 1)],
]


def tetromino(x, y, tet):
    temp = arr[x][y]

    for dx, dy in tet:
        nx = dx + x
        ny = dy + y
        if 0 <= nx < N and 0 <= ny < M:
            temp += arr[nx][ny]
        else:
            return 0  # 범위 벗어날 경우 tetromino 함수 종료
    return temp


ans = 0
for i in range(N):
    for j in range(M):
        for t in tetris:
            temp = tetromino(i, j, t)
            ans = max(temp, ans)

print(ans)
