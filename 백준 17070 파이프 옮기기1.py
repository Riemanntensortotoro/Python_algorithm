N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
dp = [[[-1 for _ in range(N)] for _ in range(N)] for _ in range(3)]

dx = [0, 1, 1] 
dy = [1, 0, 1]

def DP_pipe(row, col, dir):
    if row == N-1 and col == N-1:
        return 1
    if dp[dir][row][col] != -1:
        return dp[dir][row][col]

    dp[dir][row][col] = 0
    
    for nxt_dir in range(3):
        nxt_row = row + dx[nxt_dir]
        nxt_col = col + dy[nxt_dir]
        
        if nxt_row >= N or nxt_col >= N:
            continue

        if nxt_dir == 0: 
            if not grid[nxt_row][nxt_col] and (dir == 0 or dir == 2):
                dp[dir][row][col] += DP_pipe(nxt_row, nxt_col, nxt_dir)
        elif nxt_dir == 1: 
            if not grid[nxt_row][nxt_col] and (dir == 1 or dir == 2):
                dp[dir][row][col] += DP_pipe(nxt_row, nxt_col, nxt_dir)
        elif nxt_dir == 2:
            if not grid[nxt_row][nxt_col] and not grid[row][nxt_col] and not grid[nxt_row][col]:
                dp[dir][row][col] += DP_pipe(nxt_row, nxt_col, nxt_dir)

    return dp[dir][row][col]

print(DP_pipe(0, 1, 0))
