from collections import deque

N, M = map(int, input().split())
graph = {}
for _ in range(M):
    A, B = map(int, input().split())
    graph.setdefault(A, []).append(B)
    graph.setdefault(B, []).append(A)

def bfs(start):
    visited = {}
    queue = deque([(start, 0)])
    total_distance = 0

    while queue:
        current, distance = queue.popleft()
        if visited.get(current):
            continue
        visited[current] = True

        total_distance += distance

        for neighbor in graph.get(current, []):
            if not visited.get(neighbor):
                queue.append((neighbor, distance + 1))

    return total_distance

# 각 노드의 케빈 베이컨 수를 계산
kevin_bacon = {}
for i in range(1, N+1):
    kevin_bacon[i] = bfs(i)

# 케빈 베이컨 수가 가장 작은 사람을 출력
print(min(kevin_bacon, key=kevin_bacon.get))
