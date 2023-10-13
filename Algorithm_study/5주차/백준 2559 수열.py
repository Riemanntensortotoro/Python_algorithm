import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

sum_K_days = sum(arr[:K])

max_sum = sum_K_days 

for i in range(K, N):
    sum_K_days = sum_K_days - arr[i - K] + arr[i]  
    max_sum = max(max_sum, sum_K_days)  

print(max_sum)
