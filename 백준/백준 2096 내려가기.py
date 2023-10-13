N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp_max = [0] * 3
dp_min = [0] * 3

dp_max[0], dp_max[1], dp_max[2] = arr[0]
dp_min[0], dp_min[1], dp_min[2] = arr[0]

for i in range(1, N):
    nxt_dp_max = [0] * 3
    nxt_dp_min = [0] * 3

    nxt_dp_max[0] = arr[i][0] + max(dp_max[0], dp_max[1])
    nxt_dp_max[1] = arr[i][1] + max(dp_max)
    nxt_dp_max[2] = arr[i][2] + max(dp_max[1], dp_max[2])

    nxt_dp_min[0] = arr[i][0] + min(dp_min[0], dp_min[1])
    nxt_dp_min[1] = arr[i][1] + min(dp_min)
    nxt_dp_min[2] = arr[i][2] + min(dp_min[1], dp_min[2])

    dp_max = nxt_dp_max
    dp_min = nxt_dp_min

print(max(dp_max), min(dp_min))
