from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(y,x, desty, destx):
    que = deque()
    que.append([y,x])
    graph[y][x] = 0
    while que:
        y, x = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if -1 < nx < M and -1 < ny < N and graph[ny][nx] == 1:
                if not visited[ny][nx]:
                    que.append([ny,nx])
                    visited[ny][nx] = True
                    graph[ny][nx] = graph[y][x] + 1
            if ny == desty and nx == destx:
                return(graph[ny][nx]+1)

N, M = map(int, input().split())

graph =[]
destx, desty = M-1, N-1

visited = []
for _ in range(N):
    visited.append(M*[False])
for _ in range(N):
    graph.append(list(map(int, input())))
print(bfs(0,0,desty,destx))