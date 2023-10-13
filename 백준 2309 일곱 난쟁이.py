lst = []
for i in range(9):
    N = int(input())
    lst.append(N)

sum_lst = sum(lst)
value = sum_lst - 100  # 찾아야 하는 두 난쟁이의 키의 합

for i in range(9):
    for j in range(i + 1, 9):
        if lst[i] + lst[j] == value:
            # 찾았다면 삭제하지 말고 일단 저장
            first = lst[i]
            second = lst[j]
            break

# 찾은 두 난쟁이를 제거
lst.remove(first)
lst.remove(second)

# 오름차순 정렬
lst.sort()

# 출력
for k in lst:
    print(k)
