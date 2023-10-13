N = int(input())
dp = [False] * (N + 1)

for i in [1, 3]:
    if i <= N:
        dp[i] = False

for j in [2, 4]:
    if j <= N:
        dp[j] = True

for i in range(5, N + 1):
    dp[i] = not (dp[i-1] and dp[i-3] and dp[i-4])

print("SK" if dp[N] else "CY")
