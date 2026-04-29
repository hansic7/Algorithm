n, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(k)]

seat = [[] for _ in range(n+1)]
for i in range(1, n+1):
    seat[i].append(i)

for _ in range(3):
    for u, v in edges:
        ui = seat[u][-1]
        vi = seat[v][-1]

        seat[u].append(vi)
        seat[v].append(ui)

for i in range(1, n+1):
    seat[i] = set(seat[i])

for i in range(1, n+1):
    ans = 0
    for j in range(1, n+1):
        if i in seat[j]:
            ans += 1
    print(ans)


# Please write your code here.

