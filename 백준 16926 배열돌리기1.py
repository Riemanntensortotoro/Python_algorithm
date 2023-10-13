N, M, R=map(int,input().split())

com = [list(map(int,input().split()))for _ in range(N)]

for k in range(R):          # R 번 회전
    s = min(N, M) // 2      # layer 수
    for j in range(s):      # 각 레이어를 순회하기 위한 반복문
        x, y = j, j
        pre=com[x][y]

        # 좌측 열, 하단 행, 우측 열, 상단 행을 차례대로 회전시킵니다.
        # 예를 들어, 좌측 열을 회전시키려면 현재의 값을 임시로 저장하고, 
        # 그 다음 값으로 덮어씁니다. 이러한 과정을 계속 반복합니다.
        # 이렇게 하면 pre에는 마지막에 회전되어야 할 값이 저장되어 있을 것이고, 
        # 이 값은 최종적으로 회전의 시작점에 덮어쓰게 됩니다.
        #좌

        for i in range(x + 1, N - j):

            tmp = com[i][j]
            com[i][j] = pre
            pre = tmp

        #하

        for i in range(y + 1, M - j):

            tmp=com[N - 1 - j][i]
            com[N - 1 - j][i] = pre
            pre=tmp

        #우

        for i in range(N - j - 2, j - 1,-1):

            tmp=com[i][M - 1 - j]
            com[i][M - 1 - j]=pre
            pre=tmp
        #상

        for i in range(M - 2 - j, j - 1,-1):

            tmp = com[j][i]
            com[j][i] = pre
            pre = tmp


for i in range(N):
    for j in range(M):
        print(com[i][j], end = ' ')
    print()