def DC(a, b, c):
    if b == 1:
        return a % c
    else:
        temp = DC(a, b // 2, c)
        if b % 2 == 0:
            return temp * temp % c
        else:
            return temp * temp * a % c

A, B, C = map(int, input().split())
print(DC(A, B, C))