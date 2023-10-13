def ncr(N, R):
    if R == 0:
        print(*c)
    elif R > N:
        return
    else:
        c[R-1] = arr[N-1]
        ncr(N-1, R-1)
        ncr(N-1, R)

arr = list(map(int, input().split()))
N = len(arr)
R = int(input())
c = [0] * R
ncr(N, R)