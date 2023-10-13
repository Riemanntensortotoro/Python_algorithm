L = int(input())
S = list(map(int, input().split()))
n = int(input())

S.sort()

good_intervals = []

good_intervals.append((S[0] - 1, 1, S[0] - 1))

for i in range(1, L):
    A, B = S[i-1] + 1, S[i] - 1
    cnt = B - A + 1
    if cnt > 0:
        good_intervals.append((cnt, A, B))

good_intervals.sort()

count = 0
for cnt, start, end in good_intervals:
    for x in range(start, end + 1):
        print(x, end=' ')
        count += 1
        if count == n:
            break
    if count == n:
        break
