n = int(input())
arr = list(map(int, input().split()))
DP = [0] * (n + 1)

for i in range(1, n + 1):
    DP[i] = DP[i - 1] + arr[i - 1]

ans = 0

for i in range(2, n):
    ans = max(ans, DP[n] - arr[0] - arr[i - 1] + DP[n] - DP[i])

for i in range(2, n):
    ans = max(ans, DP[n] - arr[-1] - arr[i - 1] + DP[i - 1])

for i in range(2, n):
    ans = max(ans, DP[i] - arr[0] + DP[n] - DP[i - 1] - arr[-1])

print(ans)
