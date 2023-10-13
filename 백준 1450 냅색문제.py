# 조합(combination) 함수를 재귀로 구현
# arr: 입력 리스트, start: 시작 인덱스, end: 종료 인덱스, total: 현재까지의 누적 합, sums: 합을 저장할 리스트
def combination(arr, start, end, total, sums):
    if start == end:
        sums.append(total)
        return
    # 현재 원소를 선택하지 않는 경우
    combination(arr, start + 1, end, total, sums)
    # 현재 원소를 선택하는 경우
    combination(arr, start + 1, end, total + arr[start], sums)

# 이진 탐색(binary search) 함수
# arr: 정렬된 리스트, target: 찾을 대상 값
def binary_search(arr, target):
    start, end = 0, len(arr) - 1
    count = 0
    while start <= end:
        mid = (start + end) // 2
        # 중앙 값이 target 이하인 경우
        if arr[mid] <= target:
            count = mid + 1
            start = mid + 1
        # 중앙 값이 target 보다 큰 경우
        else:
            end = mid - 1
    return count

N, C = map(int, input().split())
weights = list(map(int, input().split()))

group1 = weights[:N//2]
group2 = weights[N//2:]

sums1, sums2 = [], []
combination(group1, 0, len(group1), 0, sums1)
combination(group2, 0, len(group2), 0, sums2)

# 리스트를 정렬
sums1.sort()
sums2.sort()

# sums1의 각 값과 짝을 이룰 수 있는 sums2의 값의 개수를 센다.
count = 0
for s in sums1:
    count += binary_search(sums2, C - s)

print(count)
