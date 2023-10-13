from collections import deque

def bfs(box, ripe_tomatoes, m, n):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    days = -1 
    q = deque(ripe_tomatoes)
    
    while q:
        size = len(q)
        for _ in range(size):
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                    box[nx][ny] = 1
                    q.append((nx, ny))
        
        days += 1 
    
    for row in box:
        if 0 in row:
            return -1
    return days

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

ripe_tomatoes = [(i, j) for i in range(n) for j in range(m) if box[i][j] == 1]

result = bfs(box, ripe_tomatoes, m, n)

print(result)
