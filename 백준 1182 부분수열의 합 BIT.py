N, S = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0

for i in range(1, 1 << N):
    subset_sum = 0

    for j in range(N):
        if i & (1 << j):
            subset_sum += nums[j]

    if subset_sum == S:
        cnt += 1

print(cnt)
