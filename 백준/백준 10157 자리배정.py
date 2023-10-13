C, R = map(int, input().split())
K = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def seat_number(C, R, K):
    if K > C * R: 
        return 0
    
    x, y = 0, 0
    dir = 0

    for _ in range(K - 1):
        nx, ny = x + dx[dir], y + dy[dir]
        
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            dir = (dir + 1) % 4
            nx, ny = x + dx[dir], y + dy[dir]

        x, y = nx, ny

    return y + 1, x + 1

x, y = seat_number(C, R, K)
print(x, y)
