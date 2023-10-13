import heapq

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
# 최소 힙(Min-Heap): 부모 노드의 키 값이 자식 노드의 키 값보다 항상 작거나 같은 완전 이진 트리

grid.sort(key=lambda x: x[0])
# 과제의 마감일(d)에 따라 힙에 과제를 추가
pqueue = []
score = 0

for d, w in grid:
    score += w
    heapq.heappush(pqueue, w)
# heappush 함수를 사용하여 힙에 원소를 추가하면 자동으로 최소 힙의 속성이 유지    
    while len(pqueue) > d:
        score -= heapq.heappop(pqueue)
# 만약 힙의 크기가 현재 과제의 마감일보다 크다면, 
# heappop 함수를 사용하여 힙에서 가장 작은 원소(가장 낮은 점수의 과제)를 제거
print(score)
