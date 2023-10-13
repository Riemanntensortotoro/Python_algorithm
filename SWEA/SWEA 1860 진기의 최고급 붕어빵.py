T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    bread = 0
    time_passed = 0
    customer_index = 0
    result = "Possible"

    while customer_index < N:
        bread += (time_passed // M) * K
        time_passed = (time_passed // M + 1) * M

        while customer_index < N and arr[customer_index] < time_passed:
            if bread > 0:
                bread -= 1
            else:
                result = "Impossible"
                break
            customer_index += 1

        if result == "Impossible":
            break

    print(f'#{tc} {result}')
