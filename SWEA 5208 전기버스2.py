def BT(station, energy, count):
    global min_count
    if station == N - 1:
        min_count = min(min_count, count)
        return
    if count >= min_count:
        return
    if energy > 0:
        BT(station + 1, energy - 1, count)
    if station < N - 1:
        BT(station + 1, board[station] - 1, count + 1)

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr[0]
    board = arr[1:]  
    min_count = float('inf') 
    BT(1, board[0] - 1, 0)
    print(f'#{tc} {min_count}')
