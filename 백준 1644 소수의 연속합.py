# 에라토스테네스의 체
N = int(input())
Aratos = [True] * (N + 1)
primes = []
for i in range(2, N + 1):
    if Aratos[i]:
        primes.append(i)
        for j in range(i * i, N + 1, i):
            Aratos[j] = False

# 두 포인터
count = 0
left, right, total = 0, 0, 0
while right < len(primes) or total >= N:
    if total < N and right < len(primes):
        total += primes[right]
        right += 1
    else:
        total -= primes[left]
        left += 1

    if total == N:
        count += 1

print(count)
