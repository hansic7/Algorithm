from collections import deque
import copy

N, M = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
visited = [[0]*M for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs(y,x):
    q = deque()
    tmp_board[y][x] = 0
    q.append([y,x])
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<M and tmp_board[ny][nx]:
                tmp_board[ny][nx] = 0
                q.append([ny,nx])

def melt(y,x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<N and 0<=nx<M and not visited[ny][nx]:
            if board[y][x] > 0:
                board[y][x] -= 1
                
tmp_board = copy.deepcopy(board)
flag = 0
for i in range(N):
    for j in range(M):
        if tmp_board[i][j]:
            bfs(i,j)
            # print(f"{z}년, tmp = {tmp_board}")
            flag +=1
            if flag > 1:
                print(0)
                exit()

      
for z in range(1, 1000):
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                visited[i][j] = True
            elif not board[i][j]:
                visited[i][j] = False

    for i in range(N):
        for j in range(M):
            if board[i][j]:
                melt(i,j)
    
    tmp_board = copy.deepcopy(board)
    flag = 0
    for i in range(N):
        for j in range(M):
            if tmp_board[i][j]:
                bfs(i,j)
                flag +=1
                if flag > 1:
                    print(z, end='')
                    exit()
print(0)