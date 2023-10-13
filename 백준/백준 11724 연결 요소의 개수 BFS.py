from collections import deque

def BFS(graph, start, visited):
    visited.add(start)
    queue = deque([start])

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

N, M = map(int, input().split())
graph = [[] for i in range(N + 1)]
visited = set()
count = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    if i not in visited:
        count += 1
        BFS(graph, i, visited)

print(count)
