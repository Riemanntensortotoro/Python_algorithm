# BFS를 시작할 노드번호를 입력받습니다.

# 출력

# 입력받은 노드를 시작으로 BFS의 순서로 방문한 노드번호들을 출력합니다.
# 단, BFS의 순서로 갈 수 있는 방법이 여러가지인 경우 작은 노드번호를 먼저 방문하는 방법으로 출력합니다.

from collections import deque

graph = [
    [0,0,0,0,1,0],
    [1,0,1,0,0,1],
    [1,0,0,1,0,0],
    [1,1,0,0,0,0],
    [0,1,0,1,0,1],
    [0,0,1,1,0,0]
]

def BFS(start, graph):
    N = len(graph)
    visited = [False] * N
    queue = deque([start])
    visited[start] = True

    while queue:
        cur = queue.popleft()
        print(cur)
        for nxt in range(N):   # 인접리스트가 아닌 인접 행렬로 입력을 받고 있기 때문
            if graph[cur][nxt] == 1 and not visited[nxt]:
                queue.append(nxt)
                visited[nxt] = True

start_node = int(input())
BFS(start_node, graph)
