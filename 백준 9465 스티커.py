T = int(input())
for _ in range(T):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        print(max(board[0][0], board[1][0]))
        continue

    DP = [[0] * n for _ in range(2)]
    DP[0][0] = board[0][0]
    DP[1][0] = board[1][0]
    DP[0][1] = board[0][1] + DP[1][0]
    DP[1][1] = board[1][1] + DP[0][0]

    for i in range(2, n):
        for j in range(2):
            DP[j][i] = board[j][i] + max(DP[1-j][i-1], DP[1-j][i-2], DP[j][i-2])

    print(max(DP[0][-1], DP[1][-1]))
