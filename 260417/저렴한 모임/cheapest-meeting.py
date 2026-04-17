import sys
INT_MAX = sys.maxsize


n, m = map(int, input().split())
v1, v2, e = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

dist_a = [[INT_MAX] * (n+1) for _ in range(n+1)]
dist_b = [[INT_MAX] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dist_a[i][i] = 0
    dist_b[i][i] = 0

for u,v,w in edges:
    dist_a[u][v] = w
    dist_a[v][u] = w
    dist_b[u][v] = w
    dist_b[v][u] = w


for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if dist_a[i][j] > dist_a[i][k] + dist_a[k][j]:
                dist_a[i][j] = dist_a[i][k] + dist_a[k][j]
            if dist_b[i][j] > dist_b[i][k] + dist_b[k][j]:
                dist_b[i][j] = dist_b[i][k] + dist_b[k][j]


cost_sum = 0

if dist_a[v1][e] == INT_MAX or dist_b[v2][e] == INT_MAX:
    print(-1)
    exit()

taxi = INT_MAX
taxi_s = 0
for k in range(1,n+1):
    if dist_a[k][e] == dist_b[k][e]:
        taxi = dist_a[k][e]
        taxi_s = k
        break

# print("k=", taxi_s)
# print("taxi=", taxi)

if taxi == INT_MAX:
    print(dist_a[k][e] + dist_b[k][e])
    exit()
else:
    print(min(dist_a[v1][taxi_s] + dist_b[v2][taxi_s] + taxi, dist_a[v1][e] + dist_b[v2][e]))


# Please write your code here.