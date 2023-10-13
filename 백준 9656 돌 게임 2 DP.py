N = int(input())
dp = [False] * (N + 1)

dp[1] = True
if N >= 3:
    dp[3] = True

for i in range(4, N + 1):
    dp[i] = not (dp[i-1] and dp[i-3])

print("CY" if dp[N] else "SK")
