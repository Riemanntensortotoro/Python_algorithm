def backtrack(start, depth):
    if depth == M:
        print(' '.join(map(str, selected)))
        return
    
    for i in range(start, N):
        selected.append(numbers[i])
        backtrack(i, depth + 1)
        selected.pop()

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort() 
selected = []

backtrack(0, 0)
