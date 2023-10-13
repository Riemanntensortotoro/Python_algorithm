import sys

input = sys.stdin.readline

M = int(input())
S = 0

for _ in range(M):
    op = input().split()
    
    if op[0] == 'add':
        S |= (1 << int(op[1]))
    elif op[0] == 'remove':
        S &= ~(1 << int(op[1]))     # 1 << k는 k 번째 bit만 켜진 상태, S의 k 번째 bit를 0으로 변경
    elif op[0] == 'check':
        print(1 if S & (1 << int(op[1])) else 0)
    elif op[0] == 'toggle':
        S ^= (1 << int(op[1]))
    elif op[0] == 'all':
        S = (1 << 21) - 1   # 1부터 20까지의 비트를 다 켜주게 만들기 (21에서 1을 빼면 됨)
    elif op[0] == 'empty':
        S = 0
