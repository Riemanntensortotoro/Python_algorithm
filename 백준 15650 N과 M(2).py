def backtrack(seq, n, m, last):
    if len(seq) == m:
        print(" ".join(map(str, seq)))
        return

    for i in range(last + 1, n + 1):
        backtrack(seq + [i], n, m, i)

n, m = map(int, input().split())
backtrack([], n, m, 0)
