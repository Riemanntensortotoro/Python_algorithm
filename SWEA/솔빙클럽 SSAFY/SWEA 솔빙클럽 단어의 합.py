from itertools import permutations
N = int(input())
words = [input() for _ in range(N)]
alpha = set()
for word in words:
    alpha.update(set(word))

max_sum = 0
for perm in permutations(range(10), len(alpha)):
    mapping = dict(zip(alpha, perm))

    total = 0
    for word in words:
        num = 0
        