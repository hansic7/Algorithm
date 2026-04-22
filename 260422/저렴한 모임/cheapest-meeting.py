import sys
INT_MAX = sys.maxsize

n, m = map(int, input().split())
v1, v2, e = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

dist = [[INT_MAX] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dist[i][i] = 0

for u,v,w in edges:
    dist[u][v] = w
    dist[v][u] = w

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

if dist[v1][e] == INT_MAX or dist[v2][e] == INT_MAX:
    print(-1)
    exit()

taxi = -1
taxi_k = 0
ans = dist[v1][e] + dist[v2][e]
for k in range(1,n+1):
    if dist[v1][k] != INT_MAX and dist[v2][k] != INT_MAX and dist[k][e] != INT_MAX:
        ans = min(ans, dist[k][e] + dist[v1][k] + dist[v2][k])

# print("k=", taxi_k)
# print("taxi=", taxi)
print(ans)
# if taxi == -1:
#     print(dist[v1][e] + dist[v2][e])
#     exit()
# else:
#     print(dist[v1][taxi_k] + dist[v2][taxi_k] + taxi)


# Please write your code here.