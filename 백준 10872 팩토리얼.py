def DP_fun(N):
    DP = [1, 1]
    for i in range(2, N + 1):
        DP.append(DP[-1] * i)
    return DP[N]

N = int(input())
print(DP_fun(N))