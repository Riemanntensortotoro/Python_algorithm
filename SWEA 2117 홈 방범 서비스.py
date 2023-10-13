T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    house = []

    def HS():
        ans = 0
        K = N + 1
        for k in range(K, 0, -1):
            cost = k * k + (k - 1) * (k - 1)
            for y in range(N):
                for x in range(N):
                    cnt = 0
                    for hx, hy in house:
                        value = abs(hx - x) + abs(hy - y)
                        if value < k:
                            cnt += 1
                    if cnt * M - cost >= 0:
                        ans = max(ans, cnt)
            if ans != 0:
                return ans
        return ans

    for i in range(N):
        for j in range(N):
            if board[i][j]:
                house.append((i, j))
    result = HS()
    print(f'#{tc} {result}')
