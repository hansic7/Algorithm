n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

dist = [[10e8] * (n+1) for _ in range(n+1)]

for u,v,w in edges:
    dist[u][v] = min(w, dist[u][v])

for i in range(1, n+1):
    dist[i][i] = 0

    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] == 10e8:
            print(-1, end = ' ')
        else:
            print(dist[i][j], end = ' ')
    print()


# Please write your code here.
