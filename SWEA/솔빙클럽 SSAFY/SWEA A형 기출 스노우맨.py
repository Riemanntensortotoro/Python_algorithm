# 스노우맨 게임은 스노우맨을 조작해서땅을 밟아가며 상,하,좌,우로 이동해서보석을 먹는 게임입니다.

# 스노우맨은 기본적으로 좌,우로는 땅이 있는 곳으로만 이동 가능합니다. 즉, 땅이 없는 곳은 좌,우로 이동할 수 없습니다.

# 게임에는 수직이동이라는 시스템이 있습니다.상,하로 이동하는 방법은 수직이동을 이용하는 것입니다. 수직이동을 하는 중에는 좌, 우로 이동할 수는 없습니다.

# 스노우맨의 수직이동에는 제한사항이 있습니다.

# 수직이동을 한 칸 할때마다 게이지는 1 씩 차오르고 LIMIT 을 넘게 되면 스노우맨은 녹아서 죽게됩니다.

# 다행하게도 땅을 밟게 되면 다시 게이지는 0으로 초기화 됩니다. 

# 스노우맨 게임을 시작하기 전에 플레이어는 수직이동 게이지의 LIMIT 을 정할 수 있습니다.

# LIMIT 을 작게 설정하면 할 수록 더 높은 점수를 얻는다고 합니다. 보석을 먹기 위한 최소 LIMIT 값을 출력해주세요.

# [제약사항]

# 1. 시작점에서 보석까지 도달할 수 없는 경우는 주어지지 않습니다.

# 2. 맵의 맨 하단부는 모든 칸들이 빈칸 없이 땅으로 되어있습니다.

# 3. 보석의 위치가 하단부의 바로 위에 주어지는 입력은 없습니다. ( 0 행이 상단, N - 1 행이 하단부일 때  N - 2 행에 주어지는 경우는 없다)

# 입력

# 첫째 줄에는 맵의 세로크기 N과 가로크기 M이 주어집니다. ( 1 <= N , M <= 50)

# 그 다음 N줄에 걸쳐 맵 정보가 주어집니다.

# 각 줄마다 M개의 숫자가 공백으로 구분되어 입력됩니다.

# 숫자는 1일 경우 땅을 의미하고 0일 경우 빈공간을 의미합니다.

# 스노우맨의 출발 지점은 2로 입력되고

# 보석이 있는 지점은 3으로 입력됩니다.

# 스노우맨과 보석이 있는 지점은 모두 땅이 있다고 가정합니다.

# 스노우맨과 보석의 입력은 한 개씩만 주어집니다.

# 출력

# 스노우맨이 보석을 먹어야 합니다.

# 수직상승 게이지의 LIMIT 최솟값을 출력해주세요.

# 스노우맨 게임은 스노우맨을 조작해서땅을 밟아가며 상,하,좌,우로 이동해서보석을 먹는 게임입니다.

# 스노우맨은 기본적으로 좌,우로는 땅이 있는 곳으로만 이동 가능합니다. 즉, 땅이 없는 곳은 좌,우로 이동할 수 없습니다.

# 게임에는 수직이동이라는 시스템이 있습니다.상,하로 이동하는 방법은 수직이동을 이용하는 것입니다. 수직이동을 하는 중에는 좌, 우로 이동할 수는 없습니다.

# 스노우맨의 수직이동에는 제한사항이 있습니다.

# 수직이동을 한 칸 할때마다 게이지는 1 씩 차오르고 LIMIT 을 넘게 되면 스노우맨은 녹아서 죽게됩니다.

# 다행하게도 땅을 밟게 되면 다시 게이지는 0으로 초기화 됩니다. 

# 스노우맨 게임을 시작하기 전에 플레이어는 수직이동 게이지의 LIMIT 을 정할 수 있습니다.

# LIMIT 을 작게 설정하면 할 수록 더 높은 점수를 얻는다고 합니다. 보석을 먹기 위한 최소 LIMIT 값을 출력해주세요.

# [제약사항]

# 1. 시작점에서 보석까지 도달할 수 없는 경우는 주어지지 않습니다.

# 2. 맵의 맨 하단부는 모든 칸들이 빈칸 없이 땅으로 되어있습니다.

# 3. 보석의 위치가 하단부의 바로 위에 주어지는 입력은 없습니다. ( 0 행이 상단, N - 1 행이 하단부일 때  N - 2 행에 주어지는 경우는 없다)

# 입력

# 첫째 줄에는 맵의 세로크기 N과 가로크기 M이 주어집니다. ( 1 <= N , M <= 50)

# 그 다음 N줄에 걸쳐 맵 정보가 주어집니다.

# 각 줄마다 M개의 숫자가 공백으로 구분되어 입력됩니다.

# 숫자는 1일 경우 땅을 의미하고 0일 경우 빈공간을 의미합니다.

# 스노우맨의 출발 지점은 2로 입력되고

# 보석이 있는 지점은 3으로 입력됩니다.

# 스노우맨과 보석이 있는 지점은 모두 땅이 있다고 가정합니다.

# 스노우맨과 보석의 입력은 한 개씩만 주어집니다.

# 출력

# 스노우맨이 보석을 먹어야 합니다.

# 수직상승 게이지의 LIMIT 최솟값을 출력해주세요.

from collections import deque

def bfs(limit, start, end, adj_dict, ground):
    queue = deque([(start, 0)])
    visited = [False] * len(ground)
    visited[start] = True

    while queue:
        now, fuel = queue.popleft()     # 현재 위치 및 사용된 연료
        if now == end:                  # 목적지에 도달한 경우
            return True
        for next_ground in adj_dict[now]: 
            if not visited[next_ground]: 
                cost = abs(ground[next_ground][0] - ground[now][0])     # 수직이동에 필요한 연료 계산
                if cost <= limit:                                       # 제한 연료 내에 이동 가능하다면
                    visited[next_ground] = True
                    queue.append((next_ground, fuel + cost))            # 큐에 추가

    return False

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

ground = []                             # 땅의 정보를 저장하는 리스트
snowman, jewelry = 0, 0
for y in range(N):
    start = False
    for x in range(M):
        if board[y][x] != 0:            # 땅 또는 스노우맨 또는 보석
            if board[y][x] == 2:        # 스노우맨 위치
                snowman = len(ground)
            if board[y][x] == 3:        # 보석 위치
                jewelry = len(ground)
            if start is False:          # 땅의 시작 지점
                start = x
            if x == M - 1 and start is not False:   # 땅의 끝 지점
                ground.append((y, start, x))
        else:                           # 빈칸인 경우
            if start is not False:
                ground.append((y, start, x - 1))
                start = False

# 각 땅의 지점이 어떤 땅의 지점과 인접한지 저장하는 딕셔너리
adj_dict = {}
for now_num, (now_y, now_start_x, now_end_x) in enumerate(ground):
    adj_list = []
    for next_num, (next_y, next_start_x, next_end_x) in enumerate(ground):
        # 서로 인접하지 않는 지점은 건너뛴다
        if next_end_x < now_start_x or next_start_x > now_end_x:
            continue
        adj_list.append(next_num)
    adj_dict[now_num] = adj_list

left, right, ans = 0, N - 1, N - 1

while left <= right:
    mid = (left + right) // 2
    if bfs(mid, jewelry, snowman, adj_dict, ground): # 연료 제한 내에서 도달 가능하다면
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)
