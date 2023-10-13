white_count = 0
blue_count = 0

def BT(x, y, n, paper):
    global white_count, blue_count
    color = paper[x][y]
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != color:
                mid = n // 2
                BT(x, y, mid, paper)
                BT(x + mid, y, mid, paper)
                BT(x, y + mid, mid, paper)
                BT(x + mid, y + mid, mid, paper)
                return
    
    if color == 0:
        white_count += 1
    else:
        blue_count += 1

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

BT(0, 0, N, paper)

print(white_count)
print(blue_count)
