def backtrack(start, sum, N, S, nums, cnt):
    if start == N:
        return cnt + 1 if sum == S else cnt

    cnt = backtrack(start + 1, sum, N, S, nums, cnt)
    cnt = backtrack(start + 1, sum + nums[start], N, S, nums, cnt)

    return cnt

N, S = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
cnt = backtrack(0, 0, N, S, nums, cnt)

# 공집합을 제외하고 출력
print(cnt - 1 if S == 0 else cnt)
