T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(N)]

    lst = []
    for i in range(N):
        bonus = 0
        count = 0
        for j in range(M):
            if board[i][j] == arr[j]:
                count += 1
                count += bonus
                bonus += 1
            else:
                bonus = 0
        lst.append(count)

    max_value = max(lst)
    min_value = min(lst)
    value = max_value - min_value
    print(f'#{tc} {value}')
