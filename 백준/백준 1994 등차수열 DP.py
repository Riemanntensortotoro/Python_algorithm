N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

dp = {}             # DP를 딕셔너리에 저장
# 3차원 DP를 2차원 DP로 차원을 내릴 수 있다
# 3차원: dp[i][j][k]로 푼다면 i는 인덱스, j는 공차, k는 등차수열의 최대길이
# 2차원: dp{(인덱스, 공차), 등차수열의 최대 길이}
max_length = 1      # 최대 길이

for i in range(N):  # i번째 항까지 중
    for j in range(i):  # j번째 항을 검토한다
        diff = arr[i] - arr[j]      # 공차 구하기
        prev_length = dp.get((j, diff), 1)  
        # 딕셔너리의 Key값으로 리스트가 불가능하므로 튜플로 저장한다
        # 딕셔너리에 (j, diff) 키가 있으면 해당하는 값을, 없으면 1을 반환한다
        cur_length = prev_length + 1
        # 위에서 반환한 값에 1을 더해 현재의 길이를 찾는다
        dp[(i, diff)] = cur_length
        max_length = max(max_length, cur_length)

print(max_length)
