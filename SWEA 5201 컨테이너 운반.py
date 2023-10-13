T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    
    container.sort(reverse=True)
    truck.sort(reverse=True)
    
    total = 0
    container_idx = 0
    truck_idx = 0
    
    # 가장 무거운 화물부터, 가장 적재용량이 큰 트럭에 실을 수 있는지 확인
    while container_idx < N and truck_idx < M:
        if container[container_idx] <= truck[truck_idx]:
            total += container[container_idx]
            container_idx += 1
            truck_idx += 1
        else:
            container_idx += 1
    
    print(f"#{tc} {total}")
