n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dist = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    graph[i][i] = 1


for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in range(n):
    for j in range(n):
        print(graph[i][j], end = ' ')
    print()

# Please write your code here.
