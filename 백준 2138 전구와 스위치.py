N = int(input())
curr = list(map(int, list(input())))
nxt = list(map(int, list(input())))

def symmetry(x):
    return 1 - x

def greedy_switch(bulbs, idx):
    for i in range(idx - 1, idx + 2):
        if 0 <= i < len(bulbs):
            bulbs[i] = symmetry(bulbs[i])

count = 0
for i in range(N - 1):
    if curr[i] != nxt[i]:
        greedy_switch(curr, i + 1)
        count += 1

if curr == nxt:
    print(count)
else:
    print(-1)
