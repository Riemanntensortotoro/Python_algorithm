# 문제

# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
# 입력

# 첫째 줄에 N이 주어진다. (1 ≤ N < 15)
# 출력

# 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

def condition(x):
    for i in range(x):    # 세로줄 거르기
    #가로줄, 대각선 체크    
        if row[i] == row[x] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True
    

def BT(num):
    global cnt
    if num == N:
        cnt += 1
        return cnt

    else:
        for i in range(N):
            row[num] = i
            if condition(num):
                BT(num + 1)

N = int(input())
row = [0] * (N)
cnt = 0

BT(0)
print(cnt)