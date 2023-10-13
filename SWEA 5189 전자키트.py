T = int(input())  # 테스트케이스의 수 T

for t in range(1, T+1):
    N = int(input())  # 구역의 수
    arr = [list(map(int, input().split())) for _ in range(N)]

    # dp[i][j]는 j라는 상태에서 i를 마지막으로 방문했을 때의 최소 배터리 소비량
    # j는 비트마스크로 표현 (예: 1101은 1, 3, 4번째 노드를 방문한 상태)
    dp = [[float('inf') for _ in range(1<<N)] for _ in range(N)]
    dp[0][1] = 0  # 초기 상태 (첫 번째 노드만 방문한 상태)

    for mask in range(1<<N):
        for cur in range(N):
            if dp[cur][mask] == float('inf'):  # 불가능한 상태는 스킵
                continue
            
            for nxt in range(N):
                if mask & (1<<nxt):  # 이미 방문한 노드는 스킵
                    continue
                next_mask = mask | (1<<nxt)
                dp[nxt][next_mask] = min(dp[nxt][next_mask], dp[cur][mask] + arr[cur][nxt])

    # 모든 노드를 방문한 뒤, 다시 첫 번째 노드로 돌아오는 최소 비용 계산
    min_cost = min(dp[i][(1<<N) - 1] + arr[i][0] for i in range(1, N))

    print(f"#{t} {min_cost}")
