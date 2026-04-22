import sys

INT_MAX = sys.maxsize

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

dist = [[INT_MAX] * (n+1) for _ in range(n+1)]

for u,v,w in edges:
    dist[u][v] = w

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

ans = INT_MAX
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            continue
        if dist[i][j] != INT_MAX and dist[j][i] != INT_MAX:
            ans = min(ans, dist[i][j] + dist[j][i])

print(ans)
# Please write your code here.
