# 코코는 한 회사의 팀의 에이스이다. 코코의 팀에연말에 급하게 완료해야 하는 업무들이 부여되었다.  

# 업무들은 단순해서 다른 부서에서 일하고 있는 직원들을 지원 받아 완료시키려 한다.

 

# 각각의 업무들은 업무 번호를 가지고 있으며 업무를 완료하는데 걸리는 소요 시간이 정해져 있다.

# 업무번호는 1부터 시작하여 1씩 증가하면서 부여된다.

 

# 업무는 독립적으로 진행이 가능한 경우도 있고 다른 업무들이 완료되어야 진행할 수 있는 업무들도 있다.

# 한 명의 직원은 하나의 업무를 맡게 되며 이 업무가 완료되기 전까지는 다른 업무를 맡을 수 없다.  

# 따라서 업무를 최대한 빨리 완료시키기 위해서는  가능한 많은 수의 직원들을 투입하여야 한다. 

# 급한 업무임으로 투입되는 직원들의 비용은 고려하지 않는다. 

 

# 빠른 진행을 위해 코코는 단 하나의 업무를 도와줄 수 있다. 

# 코코의 실력은 출중하기에, 코코가 도와주는 업무의 소요시간은 반으로 줄어든다.

 

# 업무를 완료하는데 필요한 소요시간과 업무를 시작하기 위해 미리 완료해야 하는 업무 목록이 주어졌을 때 코코와 직원들이 투입되어  전체 업무를 완료시키기 위해 필요한 최소 소요시간을 구하는 프로그램을 작성하여라. 
# [제약 사항]

# 1. 주어지는 업무의 개수 N은 1개 이상 50개 이하이다.(1 ≤ N ≤ 50)

# 2. 업무 번호는 1부터 N까지의 숫자로 나타내며, 중복되는 경우는 없다.

# 3. 업무별 소요시간은 2이상 1,000 이하의 정수로 주어진다.

# 4. 업무별 미리 완료해야 하는 업무의 개수 M은 0개 이상 N-1개 이하이다. (0 ≤ M ≤ N-1)

# 5. 투입할 수 있는 직원의 수는 제한이 없으며, 비용도 무시한다.

# 6. 한 명의 직원이 한번에 하나의 업무 만을 맡을 수 있으며, 업무가 끝나기 전에는 다른 업무를 맡을 수 없다.

# 7. 코코는 단 하나의 업무만 도와줄 수 있으며, 이 때 도와주는 업무의 소요시간은 반으로 줄어든다.

# 8. 소요 시간이 홀수인 경우 반으로 줄어들 때 소수점 이하는 제외된다. (예 : 소요시간 25 à 반으로 줄어들면 12)

# 입력

# 입력의 가장 첫 줄에는 총 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터는 각 테스트 케이스가 주어진다.

# 테스트 케이스의 첫째 줄에는 완료해야 하는 업무의 수 N이 주어진다.

# 그 다음 N개의 줄에는 1부터 N까지의 업무번호 순으로 업무의 정보가 주어진다.

# 각 줄에는 업무 소요시간, 미리 완료해야 하는 업무들의 개수 M이 주어지고, 미리 완료해야 하는 업무 번호 M개가 공백으로 구분되어 나열된다. 

# 미리 완료해야 하는 업무번호는 정렬되어 있지 않음에 유의하라.

 

# 출력

# 테스트 케이스 T에 대한 결과는 “#T”을찍고, 한 칸 띄고, 정답을 출력한다. (T는 테스트케이스의 번호를 의미하며 1부터 시작한다. )

# 정답은 모든 업무를 완료하기 위해 필요한 최소 소요시간이다. (모든 업무를 완료할수 없는 경우 -1을 출력한다.)


def BT(lst, pre, worktime, visited, dp):
    if dp[lst]:                         # 이미 계산된 작업에 대한 시간이 있다면, 그 값을 반환합니다.
        return dp[lst]
    
    if not pre[lst]:                   # 현재 작업에 사전 작업이 없다면, 작업 시간 반환
        dp[lst] = worktime[lst]
        return dp[lst]

    if visited[lst]:                    
        # 이미 방문한 작업을 다시 방문한다면
        # -1을 반환하여 순환이 있음을 표시
        return -1

    visited[lst] = True
    max_time = 0

    for next_task in pre[lst]:                # 현재 작업의 모든 사전 작업들에 대해
        time = BT(next_task, pre, worktime, visited, dp)
        if time == -1:
            return -1
        max_time = max(max_time, time)

    visited[lst] = False
    dp[lst] = max_time + worktime[lst]
    return dp[lst]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    worktime = [0]
    pre = [[] for _ in range(N + 1)]

    for i in range(N):
        board = list(map(int, input().split()))
        worktime.append(board[0])
        for j in board[2:]:
            pre[i + 1].append(j)

    answer = float('inf')

    for i in range(1, N + 1):
        dp = [0] * (N + 1)
        original = worktime[i]
        worktime[i] //= 2                     # 각 작업의 작업 시간을 절반으로


        max_time = 0
        for j in range(1, N + 1):
            visited = [False] * (N + 1)
            temp = BT(j, pre, worktime, visited, dp)
            if temp == -1:                    # 순환이 발견되면 루프를 종료
                answer = -1
                break
            max_time = max(max_time, temp)

        if answer == -1:					 # 순환이 발견되면 루프를 종료
            break
        worktime[i] = original              # 현재 작업(i)의 원래 작업 시간을 복원
        answer = min(answer, max_time)

    print(f"#{tc} {answer}")