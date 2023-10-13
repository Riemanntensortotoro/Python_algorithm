def backtrack(row, current_cost):
    global min_cost
    
    # 이미 현재 비용이 최소 비용보다 크다면 더 이상 진행하지 않음
    if current_cost > min_cost:
        return
    
    # 모든 제품에 대한 생산 비용을 계산했다면
    if row == N:
        min_cost = min(min_cost, current_cost)
        return

    # 해당 제품을 각 공장에서 생산할 경우의 비용을 계산
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            backtrack(row+1, current_cost+costs[row][i])
            visited[i] = False

T = int(input())  

for tc in range(1, T+1):
    N = int(input())  
    costs = [list(map(int, input().split())) for _ in range(N)]
   
    visited = [False] * N  
    min_cost = float('inf')  
    backtrack(0, 0) 
    print(f"#{tc} {min_cost}")  
