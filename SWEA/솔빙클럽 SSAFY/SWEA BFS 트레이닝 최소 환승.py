# 민철이는 1번 지역에서 N번 지역에 있는 회사로 매일 출근합니다.

# 현재 직장을 오래 다녔던 민철이는 각 지역의 대중교통이 어떻게 연결되어 있는지 전부 알고 있기에 어느 상황에서든 최소로 환승하여 출근합니다.

# 예를 들어, 지역을 원으로 나타내고 각 지역끼리 대중교통으로 이동하는 관계를 선으로 이어 표현한 아래와 같은 교통 지도가 있습니다.

# 출발지역은 1번이고, 도착지역인  N번 지역은 8번 입니다.

# 어느날 T지역에 큰 화재가 발생하여 T번 지역으로 환승할 수 없게 되었습니다.

# 민철이는 T번 지역을 피해 회사로 최대한 환승을 적게 하여 출근하고자 할 때,

# 그 최소 환승 횟수를 출력하는 프로그램을 작성해 주세요.

# 입력

# 첫 번째 줄에 지역의 수 N과 대중교통으로이동 가능한 관계의 수 M이 공백을 구분으로 주어집니다.(1 ≤ N ≤ 10 , 0≤ M≤ 45)

# 두 번째 줄부터 M개의 줄에 걸쳐에 정수 A, B가 공백을 구분으로 주어지며 A와 B는서로 간에대중교통으로 1번의 환승으로 갈 수 있다는 것을 의미합니다. (1≤ A,B≤ N)

# 단, A와 B가 같은 경우는 존재하지 않습니다.

# 마지막 줄에 화재가 발생한 지역 T가 주어집니다.(1 <T )

# 출력

# T번 지역을 피해 N번 지역으로 출근할 수 있는 최소 환승을 출력합니다.

# 단, 출근할 수 있는 방법이 없다면 -1을 출력합니다.

from collections import deque

def bfs(graph, fire):
    N = len(graph)
    visited = [False] * N
    queue = deque([(0, 0)])
    visited[0] = True

    while queue:
        cur, transfer = queue.popleft()

        if cur == N - 1:
            return transfer

        for nxt in graph[cur]:
            if not visited[nxt] and nxt != fire:
                visited[nxt] = True
                queue.append((nxt, transfer + 1))

    return -1

N, M = map(int, input().split())
graph = [[] for _ in range(N)] 
for _ in range(M):
    A, B = map(int, input().split())
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)  

T = int(input()) - 1 

print(bfs(graph, T))
