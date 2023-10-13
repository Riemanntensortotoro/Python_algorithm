# 정원사 코코는 아름다운 정원을 만드는 것으로 매우 유명합니다.

# 코코가 최고의 정원사라는 타이틀을 얻을 수 있었던 비결은 바로 "마법의 물뿌리개" 덕분입니다. 

 

# 코코는 하루에 단 한 번, 하나의 나무에 마법의 물뿌리개를 사용하여 물을 줄 수 있습니다. 

# 이 물뿌리개를 활용하여 나무에 물을 주면, 물을 준 날짜에 따라 나무가 쑥쑥 자랍니다.

 

#     첫째 날에 물을 준 나무는 키가 1만큼 자랍니다.
#     둘째 날에 물을 준 나무는 키가 2만큼 자랍니다.
#     셋째 날에 물을 준 나무는 키가 1만큼 자랍니다. 

 

# 위와 같이 홀수 번째 날에 물을 준 나무는 키가 1만큼 자라고, 짝수 번째 날에 물을 준 나무는 키가 2만큼 자랍니다. 

# 물론 어떤 날에는 마법의 물뿌리개를 사용하지 않을 수도 있습니다. 

 

# 코코는 아름다운 정원을 꾸미기 위해, 먼저, N개의 나무를 모두 같은 크기로 키운 후, 정원을 아름답게 만드는 작업을 시작합니다. 

 

# N개의 나무의 정보가 주어졌을 때, 모든 나무의 키가 초기의 키가 가장 컸던 나무와 같아지도록 만들기 위한 최소 날짜 수를 계산하시오.

# [제약사항] 

 

# 1. 나무의 개수 N은 2 이상 100 이하로 주어집니다. (2 ≤ N ≤ 100) 

# 2. 주어지는 나무의 초기 높이는 1 이상 120 이하입니다. 

# 입력

# 가장 첫 줄에는 테스트 케이스의 총 수가 주어집니다. 

# 그 다음 줄부터 각 테스트 케이스가 주어지며, 각 테스트 케이스는 2줄로 구성됩니다. 

# 각 테스트 케이스의 첫번째 줄에는 나무의 개수 N이 주어집니다. 

# 다음 줄에는 나무들의 높이가 공백으로 분리되어 N개의 자연수로 주어집니다. 

# 출력

# 출력의 각 줄은 ‘#x’로 시작하고(x = 테스트 케이스의 번호, 1부터 시작) 공백을 한 칸 둔 다음 가능한 최소 날짜 수를 출력합니다.

T = int(input())

def adjust_tree(lst, decrement, condition):
    for i in range(len(lst)):
        if condition(lst[i]):
            lst[i] -= decrement
            return True
    return False

for tc in range(1, T + 1):
    N = int(input())
    namu = list(map(int, input().split()))

    # 목표 높이를 가장 높은 나무의 높이로 설정
    goal = max(namu)
    # 각 나무가 목표 높이에 도달하기 위해 필요한 높이 차이 계산
    lst = [goal - n for n in namu]

    day = 0                 # 소요되는 총 일수
    is_odd_day = True       # 홀수 일 여부

    # 모든 나무가 목표 높이에 도달할 때까지 반복
    while sum(lst) > 0:
        # 홀수 일인 경우
        if is_odd_day:
            # 높이가 1인 나무를 1만큼 감소
            if not adjust_tree(lst, 1, lambda x: x == 1):
                # 홀수 높이를 가진 나무를 1만큼 감소
                if not adjust_tree(lst, 1, lambda x: x % 2 == 1 and x > 0):
                    # 짝수 높이를 가진 나무를 1만큼 감소
                    adjust_tree(lst, 1, lambda x: x % 2 == 0 and x > 2)
        # 짝수 일인 경우
        else:
            # 높이가 2인 나무를 2만큼 감소
            if not adjust_tree(lst, 2, lambda x: x == 2):
                # 짝수 높이를 가진 나무를 2만큼 감소
                if not adjust_tree(lst, 2, lambda x: x % 2 == 0 and x > 0):
                    # 홀수 높이를 가진 나무를 2만큼 감소
                    adjust_tree(lst, 2, lambda x: x % 2 == 1 and x > 1)

        # 하루가 지남
        day += 1
        is_odd_day = not is_odd_day

    print(f'#{tc} {day}')


# 도희 풀이
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     tree = list(map(int, input().split()))
#     max_t = max(tree)
#     tree_c = list(map(lambda x:max_t-x, tree))
#     # 가장 키 큰 나무와의 차 리스트

#     day = 0
#     left = []
#     cnt1 = 0

#     for c in tree_c:
#         if c != 0:
#             if c % 2:
#                 left.append(c-1)
#                 cnt1 += 1
#             else:
#                 left.append(c)
#     # 일단 홀수들은 무조건 1을 한 번 빼야 하므로 걸러내며 cnt1에 개수를 저장

#     evensum = sum(left) - cnt1 * 2
#     # 남은 짝수들의 합에서 cnt1 개수만큼의 2를 뺐을 때의 값을 저장

#     if cnt1 > 0 and evensum < 0:
#         day = cnt1 * 2 - 1
#         # 이 값이 0보다 작다면 1이 더 많으므로, 1의 개수 * 2 - 1 이 답
#     elif evensum == 0:
#         day = cnt1 * 2
#         # 이 값이 0이라면 1과 2의 개수가 같으므로, 1의 개수 * 2 이 답
#     else:
#         day = cnt1 * 2
#         # 이 값이 0보다 크다면 세트 완성 이후부터 다시 계산

#         if evensum % 6 == 0:
#             day += (evensum//6) * 4
#         elif evensum % 6 == 4:
#             day += (evensum//6) * 4 + 3
#         elif evensum % 6 == 2:
#             day += (evensum//6) * 4 + 2
#         # 6을 기준으로 순환하므로

#     print(f'#{tc}', day)