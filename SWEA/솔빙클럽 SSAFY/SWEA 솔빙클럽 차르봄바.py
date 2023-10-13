dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())
for tc in range(1, T + 1):
    N, P = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    def bomb(x, y, board):
        count = board[x][y]
        for i in range(4):
            for j in range(1, P + 1):
                nx = x + dx[i] * j
                ny = y + dy[i] * j
                if 0 <= nx < N and 0 <= ny < N:
                    count += board[nx][ny]
        return count

    value = []
    for x in range(N):
        for y in range(N):
            value.append(bomb(x, y, board))
    result = max(value)
    print(f'#{tc} {result}')