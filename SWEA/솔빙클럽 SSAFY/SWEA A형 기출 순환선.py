# 코딩선은  N개의 지하철 역을 순환하는 순환선이다. 

# 이 순환선을 사용하는 사람들이 매우 많아, "지옥철"이라고 불리우며 출퇴근 시간의 시민들을 고통스럽게 하고 있다.

# 그리하여 시에서 해당 순환선에서 2개의 직통 노선을 추가로 건설하려고 한다. 

# 직통 노선이란 하나의 역과 다른 하나의 역을 바로 연결시키는 새로운 노선이다. 

 

# 단, 최고의 효율을 낼 수 있도록, 2개의 직통 노선은 "타당도" 가 가장 높게 되도록 건설하려고 한다.

# 노선의 타당도는 (A + B)^2 + (C+D)^2 로 계산하며, A, B, C, D는 각각 한 역의 이용객 숫자를 의미한다.

 

# 또한, 직통 노선을 건설하기 위해서는 아래와 같은 조건이 충족되어야만 한다. 

# [제약 사항]


# 1. 8 ≤ N ≤ 20
# 2. 지하철 역의 이용객 숫자는 1 이상 1,000 이하이다.

# 입력

# 첫번째 줄에 test case의 개수 T (1 <= T <= 50) 가 공백으로 구분되어 주어진다. 

# 다음 줄부터 각 test case에 대한 정보가 주어진다. 

# 각 test case의 첫번째 줄에는 N이 주어진다.

# 다음 줄에는 N개의 역의 이용자 수가 순서대로 주어진다. 

# 출력

# 각 test case에 대하여 "#"와 test case의 번호 (1번부터 시작)와 공백을 둔 후, 직통 노선을 건설했을 때의 최고의 타당도를 출력한다. 

def is_valid_combination(i, j, k, l, N):
    # 다음 조건을 모두 만족하면 조합이 유효하지 않는다
    return not any([
        # 1. 같은 역을 중복 사용하는 경우
        i == k, i == l, j == k, j == l,

        # 2. 직통 노선이 중첩되는 경우
        k in range(i+1, j) and l in range(j+1, N),
        l in range(i+1, j) and k in range(j+1, N),

        # 3. 역 사이에 다른 역이 중간에 위치한 경우
        abs(i-k) == 1, abs(i-k) == N - 1, abs(i-l) == 1, abs(i-l) == N - 1,
        abs(j-k) == 1, abs(j-k) == N - 1, abs(j-l) == 1, abs(j-l) == N - 1,

        # 4. 순환선의 처음과 끝을 직통으로 연결하는 경우
        j - i == N - 1, l - k == N - 1
    ])

T = int(input()) 
for tc in range(1, T+1):
    N = int(input())  
    A = list(map(int, input().split()))  
    max_val = 0  

    for i in range(N-2):
        for j in range(i+2, N):
            for k in range(i+1, N-2):
                for l in range(k+2, N):
                    if is_valid_combination(i, j, k, l, N):
                        val = (A[i] + A[j]) ** 2 + (A[k] + A[l]) ** 2
                        max_val = max(max_val, val) 

    print(f'#{tc}', max_val) 
