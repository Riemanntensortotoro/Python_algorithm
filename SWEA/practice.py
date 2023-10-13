from collections import deque

def BFS(start, graph):
    visited = [False] * 100001
    queue = deque([(start, 0)])
    visited[start] = True

    while queue:
        cur, level = queue.popleft
        
