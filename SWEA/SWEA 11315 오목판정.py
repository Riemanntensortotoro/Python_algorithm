dx = [1, 1, 1, 0]
dy = [-1, 0, 1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]

    def Omak(x, y, board):
        for i in range(4):
            count = 1
            for j in range(1, 5):
                nx = x + dx[i] * j
                ny = y + dy[i] * j
                if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 'o':
                    count += 1
                else:
                    break
            if count >= 5:
                return True
        return False
    
    found = False
    for x in range(N):
        for y in range(N):
            if board[x][y] == 'o' and Omak(x, y, board):
                found = True
                break
        if found:
            break
    print(f'#{tc} {"YES" if found else "NO"}')