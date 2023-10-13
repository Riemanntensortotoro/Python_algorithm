N = int(input())
P = list(map(int, input().split()))
P.sort()
result = 0
for i in range(len(P)):
    result += P[i] * (len(P) - i)

print(result)