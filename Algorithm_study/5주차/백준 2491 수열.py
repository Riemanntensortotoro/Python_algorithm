N = int(input())
arr = list(map(int, input().split()))

count = 1
lst_up = []
for i in range(N-1):
    if arr[i] <= arr[i+1]:
        count += 1
    else:
        lst_up.append(count)
        count = 1
lst_up.append(count) 

count = 1  
lst_down = []
for i in range(N-1):
    if arr[i] >= arr[i+1]:
        count += 1
    else:
        lst_down.append(count)
        count = 1
lst_down.append(count)

result = max(max(lst_up), max(lst_down))
print(result)
