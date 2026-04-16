n, m = map(int, input().split())

# Create 2D list with 1-based indexing
dist = [[0] * (n + 1) for _ in range(n + 1)]

# Read distance matrix
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(n):
        dist[i][j + 1] = row[j]

# Read queries
queries = [tuple(map(int, input().split())) for _ in range(m)]


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i,j in queries:
    print(dist[i][j])

# Please write your code here.
