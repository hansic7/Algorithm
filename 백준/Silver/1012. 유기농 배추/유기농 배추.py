from collections import deque

N = int(input())

def bfs(y,x):
    que = deque()
    que.append([y,x])
    graph[y][x] = 0
    while que:
        yy, xx = que.popleft()
        for i in range(4):
            ny = yy + dy[i]
            nx = xx + dx[i]
            if -1 < nx < n and -1 < ny < m and graph[ny][nx] == 1:
                que.append([ny,nx])
                graph[ny][nx] = 0

for i in range(N):
    n, m, how_many = map(int, input().split()) 
    graph = []
    for i in range(m):
        graph.append(n * [0])

    for i in range(how_many):
        a, b = map(int, input().split())
        graph[b][a] = 1

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    cnt = 0
    for yy in range(m):
        for xx in range(n):
            if graph[yy][xx] == 1:
                cnt += 1
                bfs(yy,xx)

    print (cnt)