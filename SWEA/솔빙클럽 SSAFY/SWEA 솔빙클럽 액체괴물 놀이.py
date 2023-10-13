import heapq

N = int(input())
arr = list(map(int, input().split()))

heapq.heapify(arr)

total = 0

while len(arr) > 1:
    A = heapq.heappop(arr)
    B = heapq.heappop(arr)
    
    new_heapq = A + B
    total += new_heapq
    
    heapq.heappush(arr, new_heapq)

print(total)
