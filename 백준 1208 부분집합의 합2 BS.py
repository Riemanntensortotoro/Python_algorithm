'''
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

arr1, arr2 = arr[:N//2], arr[N//2:]

# 재귀를 이용한다
def subset_sum(nums, idx, total, result):               # idx는 현재 처리중인 원소의 인덱스
    if idx == len(nums):
        result.append(total)
        return
    subset_sum(nums, idx+1, total, result)              # 현재 원소를 부분집합에 포함시키지 않는 경우
    subset_sum(nums, idx+1, total+nums[idx], result)    # 현재 원소를 부분집합에 포함시키는 경우

sum1, sum2 = [], []
subset_sum(arr1, 0, 0, sum1)
subset_sum(arr2, 0, 0, sum2)

# sum2에서 합이 S - x인 원소의 개수를 계산하여 count에 더하기
count = 0
for x in sum1:
    count += sum2.count(S - x)  # sum2에서 S-X가 몇번 나타나는지 count메서드로 확인

# S가 0인 경우 공집합을 제외해야 하므로 count에서 1을 빼기
if S == 0:
    count -= 1

print(count)
'''
from bisect import bisect_left, bisect_right
from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))

arr1, arr2 = arr[:N//2], arr[N//2:]

# 가능한 모든 부분수열의 합
sum1, sum2 = [], []
for i in range(len(arr1) + 1):
    for c in combinations(arr1, i):  # arr1의 i개 원소로 만들 수 있는 부분수열의 조합
        sum1.append(sum(c))  # 해당 부분수열의 합을 sum1에 추가
for i in range(len(arr2) + 1):
    for c in combinations(arr2, i):  # arr2의 i개 원소로 만들 수 있는 부분수열의 조합
        sum2.append(sum(c))  # 해당 부분수열의 합을 sum2에 추가

# sum2는 이진 탐색을 사용하기 위해 정렬
sum2.sort()

# sum1의 각 원소에 대해 sum2에서 S - 원소 값의 개수를 찾아서 count에 더함
count = 0
for x in sum1:
    # sum2에서 S - x 값을 가진 원소의 개수를 찾아서 count에 더함
    count += bisect_right(sum2, S - x) - bisect_left(sum2, S - x)
    # bisect_left : sum2 에 S - x와 같은 값이 여러개 있다면 가장 왼쪽의 인덱스를 반환
    # bisect_right : sum2 에 S - x와 같은 값이 여러개 있다면 가장 오른쪽의 바로 다음 인덱스를 반환

# S가 0인 경우, 전체 수열이 아닌 빈 수열도 포함되므로 결과에서 1을 빼줌
if S == 0:
    count -= 1

print(count)