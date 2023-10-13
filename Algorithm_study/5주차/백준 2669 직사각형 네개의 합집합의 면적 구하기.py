arr = [[0] * 100 for _ in range(100)]
for num in range(4):
    ax, ay, bx, by = map(int, input().split())
    for i in range(ax, bx):
        for j in range(ay, by):
            arr[i][j] = 1

count = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            count += 1
print(count)