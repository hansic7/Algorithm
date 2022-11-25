from collections import deque

K = int(input())
W, H = map(int, input().split())


board = [list(map(int, input().split())) for _ in range(H)]

visited =[[[0]*31 for i in range(W)] for j in range(H)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
d1 = [-2, -1, 1, 2, 2, 1, -1, -2]
d2 = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs():
    q = deque()
    q.append([0,0,K])
    while q:
        y, x, z = q.popleft()
        
         
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<H and 0<=nx<W:
                if not board[ny][nx] and not visited[ny][nx][z]:
                        visited[ny][nx][z] = visited[y][x][z]+1
                        q.append([ny, nx, z])
        if y == H-1 and x == W-1:
            print(visited[y][x][z])
            exit() 
        if 0 < z:
            for i in range(8):
                ny = y + d1[i]
                nx = x + d2[i]
                if 0<=ny<H and 0<=nx<W:
                    if not board[ny][nx] and not visited[ny][nx][z-1]:
                        visited[ny][nx][z-1] = visited[y][x][z] + 1
                        q.append([ny,nx, z-1])

        
       

    print(-1)

bfs()