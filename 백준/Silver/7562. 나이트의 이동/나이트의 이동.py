from collections import deque

N = int(input())

dx = [-2,-2,-1,-1,1, 1, 2,2]
dy = [ 1,-1,-2, 2,2,-2,-1,1]

def bfs(y,x, desty, destx):
    que = deque()
    que.append([y,x])
    visited[y][x] = 0
    while que:
        y, x = que.popleft()
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if -1 < nx < I and -1 < ny < I and not visited[ny][nx]:
                que.append([ny,nx])
                visited[ny][nx] = visited[y][x] + 1
            if ny == desty and nx == destx:
                return(visited[ny][nx])
               

for i in range(N):
    I = int(input())
    nowx, nowy = map(int, input().split())
    destx, desty = map(int, input().split())

    visited = []
    for i in range(I):
        visited.append([False]*I)
    
    if nowx == destx and nowy==desty:
        print (0)
    else:
        print(bfs(nowy, nowx, desty, destx))