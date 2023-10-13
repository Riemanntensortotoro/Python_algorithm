T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    sample = list(map(str, input().split()))
    passcode = list(map(str, input().split()))

    idx = 0
    value = 0
    for i in range(N):
        if sample[i] == passcode[idx]:
            idx += 1
        if idx == K:
            value = 1
            break
    print(f'#{tc} {value}')