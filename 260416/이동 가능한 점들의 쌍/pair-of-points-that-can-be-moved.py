n, m, P, Q = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(m)]
queries = [tuple(map(int, input().split())) for _ in range(Q)]


dist = [[10e8] * (n + 1) for _ in range(n+1)]
red_dot = [[0] * (n+1) for _ in range(n+1)]


for i in range(1, n+1):
    dist[i][i] = 0
    if i <= P:
        for j in range(1, n+1):
            red_dot[i][j] = 1

for u,v,w in edges:
    dist[u][v] = w
    if red_dot[u][u] or red_dot[v][v]:
        red_dot[u][v] = 1


for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                red_dot[i][j] = max(red_dot[i][k], red_dot[k][j])

possible_sum, dist_sum = 0,0
for u,v in queries:
    if red_dot[u][v] and dist[u][v] != 10e8:
        possible_sum += 1
        dist_sum += dist[u][v]

print(possible_sum)
print(dist_sum)



# Please write your code here.
