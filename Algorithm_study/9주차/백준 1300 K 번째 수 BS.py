def count_lower(x, n):  # n x n 행렬에서 주어진 값 x보다 작거나 같은 원소의 개수를 계산하여 반환하는 함수
    count = 0
    for i in range(1, n+1):         # 행의 인덱스
        count += min(x // i, n)     # 각 행은 i * 1, i * 2, i * 3 등으로 이루어져있기 때문에
        # 행의 원소들을 각각 i로 나누는 몫은 1, 2, 3 가 되기 때문에
        # 개수를 세기 위해서는 x를 i로 나눈 몫을 세면 된다
        # 하지만 i의 배수는 최대 n개까지만(n * n 배열) 존재하기 때문에 min값으로 처리를 해야한다
    return count

def binary_search(n, k):    # mid 이하의 값의 개수가 k가 되도록 조정하자
    low, high = 1, n * n    # 1차원 배열로 변경했기 때문에 크기는 n * n이다
    result = 0
    while low <= high:
        mid = (low + high) // 2
        if count_lower(mid, n) < k: 
            low = mid + 1
        else:
            result = mid    # 동일한 값이 존재할 수 있기 때문에 result를 저장 후
            high = mid - 1  # 왼쪽으로 이동해보자
    return result           # 이 때 while에서 탈출하게 된다면 result 값을 반환 

N = int(input())
K = int(input())
print(binary_search(N, K))