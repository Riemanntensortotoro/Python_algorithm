from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y, grid, distance):
    n, m = len(grid), len(grid[0])
    queue = deque([(x, y)])
    distance[x][y] = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != 0 and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

distance = [[-1 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            target_x, target_y = i, j

BFS(target_x, target_y, grid, distance)

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()
