# 양봉업에 종사하는 코코씨는 벌집을 분양하고 있습니다.  한 사람에게 분양을 할 때, 총 4 칸의 이어져 있는 벌집을 가위로 오려내어 분양을 합니다.

# 이어져 있는 벌집을 오린다는 것은 4 칸의 벌집이 서로 떨어지지 않게 하나의 묶음으로 오린다는 것입니다.

 

# 각 벌집 칸에는 벌들의 숫자가 써져 있습니다. 벌집 판매 가격은 벌들 숫자의 합으로 계산됩니다.

# 4칸의 벌집을 오려내어 판매할 때 코코가 얻을 수 있는 가장 비싼 가격은 얼마인지 출력해주세요.

# 입력

# 벌집 정보가 2차원 배열 형태로 입력됩니다.

# 첫 번째 줄에는 2차원 배열의 세로 크기 N 과 가로크기 M 이 입력됩니다. ( 3 <= N, M <= 15 )

# 이어서 N 줄에 걸쳐 각 줄마다 M 개의 양의 정수가 공백으로 구분되어 입력됩니다. ( 양의 정수 <= 10,000,000 )
 

# 출력

# 4칸을 오려내서 벌집을 판매할 때 얻을 수 있는 최대 금액을 출력해주세요.
T = int(input())
dx_even = [-1, -1, 0, 1, 0, -1]
dy_even = [0, -1, -1, 0, 1, 1]
dx_odd = [-1, 0, 1, 1, 1, 0]
dy_odd = [0, -1, -1, 0, 1, 1]


def dfs(x, y, cnt, total, visited, arr, N, M):
    global answer
    if cnt == 4:
        answer = max(answer, total)
        return

    dx, dy = dx_even if y % 2 == 0 else dx_odd, dy_even if y % 2 == 0 else dy_odd
    for i in range(6):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, cnt + 1, total + arr[nx][ny], visited, arr, N, M)
            visited[nx][ny] = 0


def check_Y_shapes(x, y, arr, N, M):
    global answer
    for i in range(6):
        for j in range(i + 1, 6):
            for k in range(j + 1, 6):
                total = arr[x][y]
                dx, dy = dx_even if y % 2 == 0 else dx_odd, dy_even if y % 2 == 0 else dy_odd
                for dx, dy in [(dx[i], dy[i]), (dx[j], dy[j]), (dx[k], dy[k])]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M:
                        total += arr[nx][ny]
    
                    answer = max(answer, total)


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    answer = 0
    for i in range(N):
        for j in range(M):
            visited[i][j] = 1
            dfs(i, j, 1, arr[i][j], visited, arr, N, M)
            check_Y_shapes(i, j, arr, N, M)
    print(f"#{tc} {answer}")