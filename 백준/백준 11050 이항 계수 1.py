N, K = map(int, input().split())
DP = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(0, N + 1):
    DP[i][1] = i
    DP[i][0] = 1
    DP[i][i] = 1

for i in range(2, N + 1):
    for j in range(1, i):
        DP[i][j] = DP[i-1][j] + DP[i-1][j-1]

print(DP[N][K])