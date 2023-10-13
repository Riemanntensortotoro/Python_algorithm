def is_bingo(arr):
    count = 0
    
    for row in arr:
        if sum(row) == 0:
            count += 1
    
    
    for col in range(5):
        if sum([arr[row][col] for row in range(5)]) == 0:
            count += 1
    
    
    if sum([arr[i][i] for i in range(5)]) == 0:
        count += 1
    if sum([arr[i][4-i] for i in range(5)]) == 0:
        count += 1

    return count >= 3


bingo = [list(map(int, input().split())) for _ in range(5)]


position = {}
for i in range(5):
    for j in range(5):
        position[bingo[i][j]] = (i, j)


called_numbers = [list(map(int, input().split())) for _ in range(5)]


call_count = 0
for row in called_numbers:
    for num in row:
        call_count += 1
        x, y = position[num]
        bingo[x][y] = 0  # 해당 위치의 값을 0으로 변경
        if is_bingo(bingo):  # 빙고가 되었는지 확인
            print(call_count)
            exit(0)
