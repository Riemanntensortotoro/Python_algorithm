def perm(i, k, R):
    if i == R:
        print(*p[:R])  
        return
    else:
        for j in range(k):
            p[i], p[j] = p[j], p[i]
            perm(i+1, k, R)
            p[i], p[j] = p[j], p[i]

p = list(map(int, input().split()))
R = int(input())
perm(0, len(p), R)
