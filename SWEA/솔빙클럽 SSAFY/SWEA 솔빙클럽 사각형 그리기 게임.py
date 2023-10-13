T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    lst = []

    for i in range(N):
        for j in range(N):
            value = board[i][j]
            for x in range(i, N):
                for y in range(j, N):
                    if board[x][y] == value:
                        answer = (x - i + 1) * (y - j + 1)
                        lst.append(answer)

    result = max(lst)
    cnt = 0
    for i in lst:
        if i == result:
            cnt += 1
    print(f'#{tc} {cnt}')
