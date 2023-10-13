T = int(input())  
for tc in range(1, T + 1):
    N = int(input())  
    tasks = [list(map(int, input().split())) for _ in range(N)]  
    
    tasks.sort(key=lambda x: x[1])
    
    count = 0  
    cur = 0  # 현재 시간 (마지막으로 완료된 작업의 종료 시간)
    
    for s, e in tasks:
        if s >= cur: 
            count += 1
            cur = e  # 작업을 수행하고 나면 종료 시간을 현재 시간으로 업데이트
            
    print(f"#{tc} {count}")
