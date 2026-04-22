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

cost_sum = 0

if dist[v1][e] == INT_MAX or dist[v2][e] == INT_MAX:
    print(-1)
    exit()

taxi = -1
taxi_s = 0
for k in range(1,n+1):
    if dist[v1][k] + dist[k][e] == dist[v1][e] \
    and dist[v2][k] + dist[k][e] == dist[v2][e]:
        if taxi < dist[k][e]:
            taxi = dist[k][e]
            taxi_s = k

# print("k=", taxi_s)
# print("taxi=", taxi)

if taxi == -1:
    print(dist[v1][e] + dist[v2][e])
    exit()
else:
    print(dist[v1][taxi_s] + dist[v2][taxi_s] + taxi)


# Please write your code here.