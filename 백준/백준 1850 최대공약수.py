def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n, m = map(int, input().split())

gcd_value = gcd(n, m)
print('1' * gcd_value)
