N = int(input())
arr = list(map(int, input().split()))

increase = [1] * N
decrease = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            increase[i] = max(increase[i], increase[j]+1)

for i in range(N-2, -1, -1):
    for j in range(N-1, i, -1):
        if arr[i] > arr[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

result = 0
for i in range(N):
    result = max(result, increase[i] + decrease[i] - 1)
# 최고점 중복 계산
print(result)
