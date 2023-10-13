N, M = map(int, input().split())
T = int(input())
locations = [list(map(int, input().split())) for _ in range(T+1)]

def linear(loc, N, M):
    d, x = loc
    if d == 1:
        return x
    elif d == 2:
        return N + M + (N - x)
    elif d == 3:
        return 2 * (N + M) - x
    else:
        return N + x

dong = linear(locations[-1], N, M)

total = 0
for loc in locations[:-1]:
    shop = linear(loc, N, M)
    total += min(abs(shop - dong), 2 * (N + M) - abs(shop - dong))

print(total)
