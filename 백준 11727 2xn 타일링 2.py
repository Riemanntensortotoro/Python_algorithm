def DP_fun(N):
    DP = [0, 1, 3]
    for _ in range(3, N + 1):
        DP.append(DP[-1] + 2 * DP[-2])
    return DP[N]
N = int(input())
result = DP_fun(N) % 10007
print(result)