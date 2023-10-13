N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

output = []

def backtrack(start, depth):
    if depth == M:
        print(" ".join(map(str, output)))
        return
    
    last = -1
    for i in range(start, N):
        if last == numbers[i]:
            continue

        last = numbers[i]
        output.append(numbers[i])
        backtrack(i, depth + 1)
        output.pop()

backtrack(0, 0)
