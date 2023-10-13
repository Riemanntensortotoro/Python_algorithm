N, K = map(int, input().split())
angles = [float(input()) for _ in range(N)]

angles.sort()
ans = float('inf')

for start_angle in angles:
    cnt = [0] * K
    for angle in angles:
        pos = (angle - start_angle + 360) % 360     # 음수가 나올 수 있으므로 360을 더해준다
        sector = int(pos // (360 / K))
        cnt[sector] += 1
    
    cnt.sort()
    ans = min(ans, cnt[-1] - cnt[0])

print(ans)
