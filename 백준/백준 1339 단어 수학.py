from collections import defaultdict

N = int(input())
board = [input().strip() for _ in range(N)]

alpha = defaultdict(int)

for word in board:
    length = len(word)
    for i in range(length):
        alpha[word[i]] += 10 ** (length - i - 1)

sorted_alpha = sorted(alpha.keys(), key=lambda x: -alpha[x])

alpha_to_num = {}
current = 9  
for alpha in sorted_alpha:
    alpha_to_num[alpha] = current
    current -= 1 

hap = 0
for word in board:
    num_str = ""
    for alpha in word:
        num_str += str(alpha_to_num[alpha])
    hap += int(num_str)

print(hap)
