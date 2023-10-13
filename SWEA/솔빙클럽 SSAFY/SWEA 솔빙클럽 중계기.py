import math

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N + 1)]
    x, y = 0, 0
    houses = []

    for i in range(N + 1):
        for j in range(N + 1):
            if board[i][j] == 2:
                x, y = i, j
            elif board[i][j] == 1:
                houses.append((i, j))

    max_distance_square = max((hx - x) ** 2 + (hy - y) ** 2 for hx, hy in houses)
    radius = int(math.ceil(math.sqrt(max_distance_square)))
    print(f'#{tc} {radius}')