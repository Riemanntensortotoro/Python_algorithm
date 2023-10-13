# 문제

# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
# 입력

# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.
# 출력

# 첫째 줄에 연결 요소의 개수를 출력한다.

N, M = map(int, input().split())
board = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    u, v = map(int, input().split())
    board[u].append(v)
    board[v].append(u)

def DFS(i):
    visited[i] = 1
    for nxt in board[i]:
        if not visited[nxt]:
            DFS(nxt)

count = 0
for j in range(1, N + 1):
    if not visited[j]:
        count += 1
        DFS(j)

print(count)