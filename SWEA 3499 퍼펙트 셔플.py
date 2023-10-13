T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(str, input().split()))
    new_arr = [0] * N  

    mid = N // 2
    if N % 2 == 1:
        mid += 1  

    for i in range(mid):
        new_arr[2 * i] = arr[i]

    for j in range(mid, N):
        new_arr[2 * (j - mid) + 1] = arr[j]

    print(f'#{tc}', *new_arr)
