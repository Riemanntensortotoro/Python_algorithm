from itertools import combinations
from collections import deque

def nCr(n, r):
    if r == 0:
        print(*c)
    elif r > n:
        return
    else:
        c[r-1] = arr[n-1]
        nCr(n-1, r)
        nCr(n-1, r-1)

arr = list(map(int, input().split()))
n = len(arr)
r = int(input())
c = [0] * r
