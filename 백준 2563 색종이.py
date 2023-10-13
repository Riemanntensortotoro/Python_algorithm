arr = [[0] * 100 for _ in range(100)]
N = int(input())
for num in range(N):
    a, b = map(int, input().split())
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            arr[i][j] = 1

count = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            count += 1
print(count)