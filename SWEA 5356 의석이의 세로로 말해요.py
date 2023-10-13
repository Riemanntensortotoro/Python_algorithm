T = int(input())
for tc in range(1, T + 1):
    board = [[' ' for _ in range(15)] for _ in range(5)] 
    for i in range(5):
        arr = input()
        for j in range(len(arr)):
            board[i][j] = arr[j]
    result = ''
    for j in range(15):
        for i in range(5):
            if board[i][j] != ' ':
                result += board[i][j]
    print(f'#{tc} {result}')