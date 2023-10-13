import heapq

def dijkstra(graph, start, end):
    distance = [float('inf')] * N
    distance[start] = 0
    q = [(0, start)]

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for next_node, cost in graph[node]:
            new_dist = dist + cost

            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(q, (new_dist, next_node))

    return distance[end]

N, T = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(T):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

result = dijkstra(graph, 0, N-1)

if result == float('inf'):
    print("impossible")
else:
    print(result)
