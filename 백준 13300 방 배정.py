from math import ceil

board = [[0 for _ in range(2)] for _ in range(6)]
N, K = map(int, input().split())
for i in range(N):
    b, a = map(int, input().split())
    board[a-1][b] += 1 

count = 0
for i in range(6):
    for j in range(2):
        count += ceil(board[i][j] / K)

print(count)
