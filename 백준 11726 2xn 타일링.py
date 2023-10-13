def DP_fibo(N):
    DP = [0, 1]
    for _ in range(2, N + 2):
        DP.append(DP[-1] + DP[-2])
    return DP[N + 1]

N = int(input())
result = DP_fibo(N) % 10007
print(result)