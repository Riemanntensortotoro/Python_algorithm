# 코딩구에는 현재 인구가 너무 많아 지자체에서 관리가 어려운 수준이다. 

# 그렇기 때문에 코딩구에 존재하는 N개의 마을을 두 개의 지역구 (지역 A, 지역 B)로 분리하여 관리를 할 예정이다. 

# 나눠진 지역구를 관리할 대표는 투표를 통해 선정하려고 한다. 단, 지역 대표 선출의 형평성을 위해, A와 B 지역구에 포함된 유권자의 수 차이가 최소가 되도록 지역을 분리하려고 한다. 

# [제약사항]

#     마을의 수 N은 4 이상, 8 이하의 정수이다. 
#     i번째 마을의 유권자 수 Pi는 1 이상, 20 이하의 정수이다.
#     마을 r과 마을 c가 인접한 경우, Rrc = 1이며, 인접하지 않은 경우 0으로 주어진다. 
#     Rrc = Rcr을 충족한다.
#     모든 마을들은 서로 인접하거나 인접한 마을을 통해 연결되어 있다.
#     모든 마을은 반드시 지역구 중 하나에 포함되어야 한다. 

 

# 입력

# 첫번째 줄에는 테스트 케이스의 개수 T가 주어진다. 

# 그리고 다음 줄 부터 T개의 테스트 케이스가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 마을의 개수 N이 주어진다.

# 다음 N개의 줄에는 마을의 연결 정보인 Rrc가 주어진다. (Rrc는 r번째 행과 c번째 열의 값을 의미한다.)

# 각 테스트 케이스의 마지막 줄에는 i번째 마을의 유권자의 수 Pi가 순서대로 주어진다. 

 

# 출력

# 테스트 케이스의 개수만큼 T개의 줄에 걸쳐 각 테스트 케이스에 대한 정답을 출력한다.

# 각 줄은 "#t"로 시작하고 (t는 1부터 시작하는 테스트 케이스의 번호를 의미한다.) 공백을 하나 둔 후, 정답을 출력한다. 

from collections import deque

def bfs(start, group):
    visited = [False] * N
    q = deque([start])
    visited[start] = True

    while q:
        cur = q.popleft()
        for nxt in range(N):
            if adj_matrix[cur][nxt] and nxt in group and not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

    for node in group:
        if not visited[node]:
            return False
    return True

def ncr(N, R):
    if R == 0:
        comb = list(c)
        A = set(comb)
        B = set(range(len(arr))) - A

        if bfs(list(A)[0], A) and bfs(list(B)[0], B):
            A_population = sum(population[v] for v in A)
            B_population = total_population - A_population
            diff = abs(A_population - B_population)
            global min_diff
            min_diff = min(min_diff, diff)
    elif R > N:
        return
    else:
        c[R-1] = arr[N-1]
        ncr(N-1, R-1)
        ncr(N-1, R)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [i for i in range(N)]
    adj_matrix = [list(map(int, input().split())) for _ in range(N)]
    population = list(map(int, input().split()))
    total_population = sum(population)
    min_diff = float('inf')

    for r in range(1, N//2+1):
        c = [0] * r
        ncr(N, r)

    print(f"#{tc} {min_diff}")
