# import bisect
# import sys
# input = sys.stdin.readline

# N = int(input())
# A = list(map(int, input().split()))

# LIS = [A[0]]

# for i in range(1, N):
#     if A[i] > LIS[-1]:  
#         LIS.append(A[i])
#     else:  
#         idx = bisect.bisect_left(LIS, A[i])
#         LIS[idx] = A[i]

# print(len(LIS))

def BS(lst, value):
    start, end = 0, len(lst) - 1

    while start <= end:
        mid = (start + end) // 2
        if lst[mid] < value:
            start = mid + 1
        else:
            end = mid - 1

    return start            # bisect left 를 구현

N = int(input())
A = list(map(int, input().split()))

LIS = [A[0]]

for i in range(1, N):
    # A[i] 값이 LIS의 마지막 값보다 큰 경우 LIS에 추가
    if A[i] > LIS[-1]:
        LIS.append(A[i])
    else:
        # idx = bisect.bisect_left(LIS, A[i])
        idx = BS(LIS, A[i])
        LIS[idx] = A[i]

print(len(LIS))