# 민철이는 이번에 새로운 직장으로 이직을 하게 되었습니다. 그는 이에 맞게 "출근하기 편한 지역"으로 이사를 가려고 합니다.
 

# 민철이는 버스로 출근하며, "K번 이하의 버스 탑승으로 출근할 수 있는 지역"을 "출근하기 편한 지역"의 기준으로 삼습니다.

# 민철이는 부동산 앱을 활용하여 출근하기 편한이사 후보 지역이 몇 곳이 있는지 찾아보려 합니다.

 

# 아래의 예시는 각 지역에 존재하는 버스 정류장(1번~10번)을 원으로 나타내고 있으며, 버스의 경로를 선으로 나타내고 있습니다.

# 모든 버스 정류장에서 다른 버스 정류장으로 이동하기 위해서는 제각각 다른 버스의 탑승이 필요합니다. 아래 예시에서는 설명의 편의를 위해 임의의 버스 번호를 부여하고 있습니다.

# 총N개의 지역에 대한 버스 노선도의 정보가 주어질 때,민철이가 편하게 출근할 수 있는 지역의 후보지가 몇 군데있는지 출력하는 프로그램을 작성해 주세요.

# 입력

# 첫 번째 줄에 지역의 수 N과 버스로 이동 가능한 관계의 수 M이 공백을 구분으로 주어집니다.(1 ≤ N≤ 10 , 0≤ M≤ 45)

# 지역의 번호는 1부터 N까지의 번호가 부여됩니다.

# 두 번째 줄부터 M개의 줄에 걸쳐정수A, B가 공백으로 구분되어 주어집니다. A와 B는 한 버스의 이동 경로를 의미하며, A에서 B 방향으로, 또는 B에서 A방향으로 이동할 수 있습니다. (1≤ A, B≤ N,A =/= B)

# 마지막 줄에직장이 존재하는 지역 R과출근하기 편하다는기준이 되는 버스 탑승 횟수 K가 공백으로 구분되어 주어집니다.(1 ≤ R≤ N , 0≤ K≤9)

# 출력

# 민철이가 출근하기 편하다고 느끼는이사 후보 지역의 개수를 출력합니다.

from collections import deque

def bfs(graph, R, K, N):
    visited = [False] * (N + 1)
    queue = deque([(R, 0)])  
    visited[R] = True
    count = 0

    while queue:
        curr, bus_count = queue.popleft()
        
        # K번 이하로 버스를 탄 경우 count 증가
        if bus_count <= K:
            count += 1

        for neighbor in graph[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, bus_count + 1))

    return count


N, M = map(int, input().split())


graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

R, K = map(int, input().split())

print(bfs(graph, R, K, N)) 
