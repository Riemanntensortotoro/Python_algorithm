T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [0] * 5001
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B + 1):
            arr[j] += 1
    P = int(input())
    lst = []
    for k in range(P):
        C = int(input())
        lst.append(arr[C])
    print(f'#{tc}', *lst)