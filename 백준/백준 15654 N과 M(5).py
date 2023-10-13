from itertools import permutations

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

# M개를 고르는 모든 수열을 생성
for perm in permutations(numbers, M):
    print(" ".join(map(str, perm)))
