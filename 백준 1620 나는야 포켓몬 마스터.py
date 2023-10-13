import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

name_to_number = {}
number_to_name = []

for i in range(1, N+1):
    name = input().strip()
    name_to_number[name] = i
    number_to_name.append(name)

for _ in range(M):
    query = input().strip()
    
    if query.isdigit():
        print(number_to_name[int(query)-1])
    else:
        print(name_to_number[query])
