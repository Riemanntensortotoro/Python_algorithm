T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    def is_rising(arr):
        str_arr = str(arr)
        for i in range(len(str_arr) - 1):
            if str_arr[i] > str_arr[i + 1]:
                return False
        return True
    
    max_value = -1
    for i in range(N):
        for j in range(i + 1, N):
            value = numbers[i] * numbers[j]
            if is_rising(value):
                max_value = max(max_value, value)
    print(f'#{tc} {max_value}')