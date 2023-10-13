T = int(input()) 

for t in range(1, T+1):
    board = [list(map(int, input().split())) for _ in range(9)]
    valid = 1  # 스도쿠가 유효하면 1, 아니면 0

    # 행과 열 검사
    for i in range(9):
        row = [0]*10
        col = [0]*10
        for j in range(9):
            row[board[i][j]] += 1
            col[board[j][i]] += 1
        if max(row) > 1 or max(col) > 1:
            valid = 0
            break

    # 3x3 서브그리드 검사
    if valid:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgrid = [0]*10
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        subgrid[board[x][y]] += 1
                if max(subgrid) > 1:
                    valid = 0
                    break
            if not valid:
                break

    print(f"#{t} {valid}")
