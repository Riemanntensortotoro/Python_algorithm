S = int(input())
arr = input().split()
N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    if a == 1:
        for k in range(1, S + 1):
            if k % b == 0:
                idx = k - 1
                arr[idx] = '0' if arr[idx] == '1' else '1'
    else:
        c = b - 1  # 중심점 인덱스
        arr[c] = '0' if arr[c] == '1' else '1'  # 중심은 무조건 바뀐다
        for k in range(1, S // 2):
            if c - k >= 0 and c + k < S and arr[c - k] == arr[c + k]:
                arr[c - k] = arr[c + k] = '0' if arr[c + k] == '1' else '1'
            else:
                break 
            
for i in range(0, len(arr), 20):
    print(" ".join(arr[i:i + 20]))
