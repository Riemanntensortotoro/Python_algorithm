# 1. 최장 공통 문자열(Longest Common Substring)
## 기본 코드
if i == 0 or j == 0:
	LCS[i][j] = 0
elif string_A[i] == string_B[j]:
	LCS[i][j] = LCS[i - 1][j - 1] + 1
else:
	LCS[i][j] = 0

## 기본 로직
문자열 A와 B를 한 글자씩 비교하여
두 문자가 다르다면 LCS[i][j]에 0 을 표시
두 문자가 같다면 LCS[i - 1][j - 1] 에 +1


# 2. 최장 공통 부분수열(Longest Common Subsequence)
## 공통 문자열 문제와의 차이점
부분수열은 연속된 값이 아니어도 된다
현재의 문자를 비교하는 과정 이전의 최대 공통 부분수열은 계속해서 유지됨
'현재의 문자를 비교하는 과정' 이전의 과정이 바로 LCS[i - 1][j]와 LCS[i][j- 1]가 된다

## 기본 코드
if i == 0 or j == 0: 
	LCS[i][j] = 0
elif string_A[i] == string_B[j]:
	LCS[i][j] = LCS[i - 1][j - 1] + 1
else:
	LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])
	
## 기본 로직
문자열A, 문자열B의 한글자씩 비교해봅니다.
두 문자가 다르다면 LCS[i - 1][j]와 LCS[i][j - 1] 중에 큰 값을 표시
두 문자가 같다면 LCS[i - 1][j - 1] 값을 찾아 +1