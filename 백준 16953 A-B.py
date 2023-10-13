from collections import deque

A, B = map(int, input().split())

queue = deque([(A, 0)]) 

while queue:
    cur, oper = queue.popleft()
    
    if cur == B:
        print(oper + 1)
        exit(0)
        
    next_num = cur * 2
    if next_num <= B:
        queue.append((next_num, oper + 1))
        
    next_num = int(str(cur) + "1")
    if next_num <= B:
        queue.append((next_num, oper + 1))

print(-1)
