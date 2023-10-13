T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    DP = [[0] * N for _ in range(N)]
    DP[0][0] = board[0][0]

    for i in range(1, N):
        DP[0][i] = DP[0][i-1] + board[0][i]
        DP[i][0] = DP[i-1][0] + board[i][0]
    
    for j in range(1, N):
        for k in range(1, N):
            DP[j][k] = min(DP[j-1][k], DP[j][k-1]) + board[j][k]
    
    result = DP[N-1][N-1]
    print(f'#{tc} {result}')