dp = [[0 for _ in range(31)] for _ in range(31)]
dp[0][0] = 1 

for n in range(31):
    for m in range(31):
        if n > 0:
            dp[n][m] += dp[n-1][m+1]
        if m > 0:
            dp[n][m] += dp[n][m-1]

while True:
    N = int(input())
    if N == 0:
        break
    print(dp[N][0])  # 완전한 약이 N개, 반쪼갠 약이 0개일 때 가능한 문자열의 개수를 출력
