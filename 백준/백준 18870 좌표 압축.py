import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

sorted_arr = sorted(list(set(arr)))

dict_arr = {sorted_arr[i]: i for i in range(len(sorted_arr))}

for a in arr:
    print(dict_arr[a], end=' ')
