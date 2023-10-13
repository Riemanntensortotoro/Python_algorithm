def npr(i, N, R):
    if i == R:
        print(*p)
    else:
        for j in range(N):
            if used[j] == 0:
                used[j] = 1                
                p[i] = arr[j]                
                npr(i+1, N, R)
                used[j] = 0

arr = list(map(int, input().split()))
N = len(arr)
R = int(input())

used = [0] * N
p = [0] * R
npr(0, N, R)
