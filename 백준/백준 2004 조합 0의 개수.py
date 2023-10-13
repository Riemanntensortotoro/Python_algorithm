n, m = map(int, input().split())

def count_factors(n, p):
    count = 0
    while n > 0:
        n //= p
        count += n
    return count

count_5 = count_factors(n, 5) - count_factors(m, 5) - count_factors(n-m, 5)
count_2 = count_factors(n, 2) - count_factors(m, 2) - count_factors(n-m, 2)

print(min(count_5, count_2))