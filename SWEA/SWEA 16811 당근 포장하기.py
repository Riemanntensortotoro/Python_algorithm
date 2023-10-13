T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    Ci = list(map(int, input().split()))
    Ci.sort()
    can = []
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            A = Ci[:i]
            B = Ci[i:j]
            C = Ci[j:]
            if A[-1] == B[0] or B[-1] == C[0]:
                continue
            if len(A) * len(B) * len(C) == 0:
                continue
            if len(A) > N // 2 or len(B) > N // 2 or len(C) > N // 2:
                continue

            can.append(max(abs(len(A) - len(B)), abs(len(B) - len(C)), abs(len(C) - len(A))))
    try:
        print(f'#{tc} {min(can)}')
    except:
        print(f'#{tc} -1')