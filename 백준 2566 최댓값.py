arr = [list(map(int, input().split())) for _ in range(9)]

max_value = 0
max_pos = [0, 0]

for i in range(9):
    for j in range(9):
        if arr[i][j] > max_value:
            max_value = arr[i][j]
            max_pos = [i+1, j+1]  


print(max_value)
print(f"{max_pos[0]} {max_pos[1]}")
