K = int(input())
row = []
col = []
total = []

for i in range(6):
    a, b = map(int, input().split())
    total.append(b)
    if a == 1 or a == 2:
        row.append(b)
    else:
        col.append(b)

# 가장 큰 가로, 세로 길이를 가진 변의 인덱스를 찾는다.
row_idx = total.index(max(row))
col_idx = total.index(max(col))

# 작은 사각형의 가로, 세로 길이를 찾는다.
small_row = abs(total[(col_idx - 1) % 6] - total[(col_idx + 1) % 6])
small_col = abs(total[(row_idx - 1) % 6] - total[(row_idx + 1) % 6])

# 큰 사각형과 작은 사각형의 넓이 차이를 구한다.
max_S = max(row) * max(col)
min_S = small_row * small_col

# 최종 참외 개수를 출력한다.
print(K * (max_S - min_S))
