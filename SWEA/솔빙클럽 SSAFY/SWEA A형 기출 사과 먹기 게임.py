# 사과 먹기 게임은 N x N 크기의 맵에서 캐릭터를 이동하여 사과를 먹는 게임이다. 

# 게임의 룰은 간단하다. 주어진 M개의 사과를 사과를 1번부터 M번 사과까지 순서대로 먹기만 하면 되는 게임이다. 

# [제한 조건]

#     5 <= N <= 10
#     1 <= M <= 10
#     사과의 번호는 1~M번까지 중간 값의 누락 없이 주어짐이 보장된다. (예 : M = 3이라면, 1 2 3 이 모두 주어짐이 보장된다.)
#     사과의 개수 M은 직접적으로 입력이 되지 않는다. 
#     사과는 N x N 크기의 맵의 테두리 부분에 주어지지 않는다. (0번 행, 0번 열, N-1번 행, N-1번 열)
#     i번째 사과와 i+1번째 사과의 위치는 같은 행, 열에 주어지지 않음이 보장된다.
#     단, i번째 사과와 i+2번째 사과의 위치는 같은 행, 열에 주어질 수 있다. 

# 입력

# 첫번째 줄에 test case의 개수 T (1 <= T <= 50) 가 공백주어진다. 다음 줄부터 각 test case에 대한 정보가 주어진다.

# 각 test case의 첫번째 줄에는 N이 주어진다.

# 다음 N개의 줄에 걸쳐 게임맵의 정보가 공백으로 구분되어 주어진다. 

# 게임맵의 정보에서 0은 이동 가능한 길을 의미하며, 1~M 사이의 정수는 플레이어가 먹어야 하는 사과의 순번을 나타낸다. 

# 출력

# 각 test case에 대하여 "#"와 test case의 번호 (1번부터 시작)와 공백을 둔 후, 주어진 게임맵에서 모든 사과를 순서대로 먹기 위해 필요한 최소한의 우회전의 수를 출력한다.
 
turncnt = [
    [3, 1, 3, 2],
    [2, 3, 1, 3],
    [1, 2, 3, 3],
    [3, 3, 2, 1]
]
nextdir = [
    [2, 3, 2, 1],
    [0, 3, 2, 3],
    [0, 3, 1, 1],
    [0, 0, 2, 1]
]
T = int(input())
for tc in range(1, T+1):
    apples = []
    board = []
    N = int(input())
    for i in range(N):
        row = list(map(int, input().split()))
        board.append(row)
        for j in range(len(row)):
            col = row[j]
            if col > 0:
                apples.append((col, i, j))
    apples.sort()
    ans = 1
    dir = 1
    y = apples[0][1]
    x = apples[0][2]
    for i in range(1, len(apples)):
        ny = apples[i][1]
        nx = apples[i][2]
        if ny < y and nx < x:
            ans += turncnt[dir][0]
            dir = nextdir[dir][0]
        if ny < y and nx > x:
            ans += turncnt[dir][1]
            dir = nextdir[dir][1]
        if ny > y and nx < x:
            ans += turncnt[dir][2]
            dir = nextdir[dir][2]
        if ny > y and nx > x:
            ans += turncnt[dir][3]
            dir = nextdir[dir][3]
        y = ny
        x = nx
    print(f"#{tc} {ans}")
