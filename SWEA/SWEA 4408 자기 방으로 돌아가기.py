T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [0] * 200

    for k in range(N):
        a, b = map(int, input().split())
        min_value = (min(a, b) - 1) // 2
        max_value = (max(a, b) - 1) // 2
        for i in range(min_value, max_value + 1):
            arr[i] += 1
    result = max(arr)
    print(f'#{tc} {result}')
