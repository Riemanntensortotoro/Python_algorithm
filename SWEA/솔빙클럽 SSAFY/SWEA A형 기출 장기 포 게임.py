# 장기 게임에서의 포(包)는 아주 중요하고 강력한 말 중 하나이다.

#1. 포는 다른 말을 하나 뛰어 넘어야만 이동이 가능하다. 

#2. 다른 하나의 말을 뛰어 넘었을 때, 해당 방향에 다른 말이 존재한다면, 해당 말을 먹을 수 있다. 

# 장기 포 게임판의 정보가 주어졌을 때, 포가 먹을 수 있는 쫄의 개수를 구하는 프로그램을 작성하라. 

# [제한사항]

#     5 <= N <= 50 
#     포는 2로 입력된다.
#     쫄은 1로 입력된다.
#     빈칸 (이동 가능한 칸) 은 0으로 입력된다.
#     포는 단 1개만 주어짐이 보장된다. 
#     쫄의 개수는 최대 N * N - 1 개 까지 주어진다. 

# 입력

# 첫번째 줄에 test case의 개수 T가 입력된다. (1 <= T <= 50)

# 두번째 줄부터 각 test case에 대한 입력이 주어진다.

# 각 test case의 첫번째 줄에는 N이 주어진다.

# 그리고 다음 줄부터 N개의 줄에 걸쳐 N x N 크기의 장기 포 게임의 게임판의 정보가 주어진다. 

# 출력

# 각 test case 에 대하여 "#x" (x는 test case의 번호를 의미, 1부터 시작)를 출력하고, 하나의 공백을 둔 후 정답을 출력한다. 

def RC(dx, dy, board, n):
    global cnt
    if n == 3:
        return
    else:
        for k in range(4):
            flag = 0        # 아직 어떤 쫄도 뛰어넘지 않음
            for l in range(1, N):
                nx = dx + dir[k][0] * l
                ny = dy + dir[k][1] * l
                if flag > 1:
                    break
                if 0 <= nx < N and 0 <= ny < N:
                    if board[nx][ny] == 1:
                        if flag == 1 and visited[nx][ny] == 0:
                            # 첫 번째로 만난 쫄이면서 아직 먹지 않은 경우
                            cnt += 1
                            visited[nx][ny] = 1
                            board[nx][ny] = 0
                            # 쫄을 먹고 다음 위치로 재귀 호출
                            RC(nx, ny, board, n+1)
                            board[nx][ny] = 1
                        elif flag == 1 and visited[nx][ny] == 1:
                            # 첫 번째로 만난 쫄이지만 이미 먹은 경우
                            board[nx][ny] = 0
                            RC(nx, ny, board, n + 1)
                            board[nx][ny] = 1
                        flag += 1
                    # 해당 위치가 빈칸이면서 이미 한 쫄을 뛰어 넘은 경우
                    if board[nx][ny] == 0 and flag == 1:
                        RC(nx, ny, board, n+1)

dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                x, y = i, j

    board[x][y] = 0
    visited = [[0] * N for _ in range(N)] 
    cnt = 0
    RC(x, y, board, 0)
    
    print(f'#{tc}', cnt)
