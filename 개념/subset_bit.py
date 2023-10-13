arr = list(map(int, input().split()))
N = len(arr)

for i in range(1, 1<<(N-1)):
    group1 = []
    group2 = []
    
    for j in range(N):
        if i & (1<<j):  # i의 j번 비트가 1이면
            group1.append(arr[j])
        else:
            group2.append(arr[j])

    print(group1, group2)