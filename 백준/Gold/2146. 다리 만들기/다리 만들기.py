from collections import deque

N = int(input())  ####
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

def bfs_edge(y,x,z):
    q = deque()
    board[y][x] = z
    visited[y][x] = True
    q.append([y,x])
    while q:
        y, x = q.popleft()
        for ny,nx in [(y,x+1), (y,x-1), (y+1,x), (y-1, x)]:
            if 0<=ny<N and 0<=nx<N and not visited[ny][nx]:
                if board[ny][nx] == 1:
                    q.append([ny,nx])
                    visited[ny][nx] = True
                    board[ny][nx] = z
                    
z = 2  ##섬에 넘버 붙여줄거임 0은바다 1은 애초섬이니 2부터 레이블링 시작
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            bfs_edge(i,j,z)
            z += 1

def bfs_bridge(z):
    q = deque()  ## 대안
    check = [[-1]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if 0<=i<N and 0<=j<N and board[i][j] == z:
                q.append([i, j])
                check[i][j] = 0
                
    while q:
        y,x = q.popleft()
        for ny,nx in [(y,x+1), (y,x-1), (y+1,x), (y-1, x)]:
            if 0<=ny<N and 0<=nx<N:
                if 0 < board[ny][nx] and z != board[ny][nx]:
                    return(check[y][x])
                if 0 == board[ny][nx] and check[ny][nx] == -1:
                    check[ny][nx] = check[y][x] + 1
                    q.append([ny,nx])
    return (0)

res = 2000 * 2000
for i in range(2, z):
    res = min(res, bfs_bridge(i))

print(res)