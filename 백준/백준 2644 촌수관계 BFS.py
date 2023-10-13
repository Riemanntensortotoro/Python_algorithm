from collections import deque

def bfs(graph, start, end):
    visited = {}
    queue = deque([(start, 0)])

    while queue:
        current, level = queue.popleft()
        if current == end:
            return level
        if current in visited:
            continue
        visited[current] = True

        for neighbor in graph.get(current, []):
            queue.append((neighbor, level + 1))
            
    return -1 

n = int(input()) 
a, b = map(int, input().split())  
m = int(input()) 

graph = {}
for _ in range(m):
    x, y = map(int, input().split()) 
    graph.setdefault(x, []).append(y)
    graph.setdefault(y, []).append(x) 

print(bfs(graph, a, b))
