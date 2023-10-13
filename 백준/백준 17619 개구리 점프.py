import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
lst = []

for i in range(N):
    a, b, c = map(int, input().split())
    lst.append({"x1": a, "x2": b, "num": i})

lst.sort(key=lambda x: x["x1"])

id = 0
e = lst[0]["x2"]

g = [0] * N
g[lst[0]["num"]] = id

for i in range(1, N):
    if lst[i]["x1"] <= e:
        if lst[i]["x2"] > e:
            e = lst[i]["x2"]
    else:
        id += 1
        e = lst[i]["x2"]
    
    g[lst[i]["num"]] = id

for _ in range(Q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if g[u] == g[v]:
        print(1)
    else:
        print(0)
