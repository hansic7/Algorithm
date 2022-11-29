from collections import deque
import copy

N,M = 5,7
dd = ['0 0 0 0 0 0 0',
      '0 0 0 3 0 0 0',
      '0 3 0 0 0 2 0',
      '0 7 6 2 4 0 0',
      '0 0 0 0 0 0 0']
board = [list(map(int, dd[i].split())) for i in range(N)]

# N, M = map(int, input().split())
# board = [list(map(int, input().split())) for i in range(N)]
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

for z in range(1, 300):   ### <-- 이 포문 때문에 시간 많이 잡아 먹는데, 
    for i in range(N):    ### 걍 ice 위치 저장해서 "while ice:"로 돌리면 시간 훨씬 줄어듬
        for j in range(M):
            if board[i][j]:
                visited[i][j] = True
            elif not board[i][j]:
                visited[i][j] = False
    # print(f"{z}년, visitd = {visited}")

    for i in range(N):
        for j in range(M):
            if board[i][j]:
                melt(i,j)
    # print(f"{z}년, board = {board}" )
    
    tmp_board = copy.deepcopy(board)
    flag = 0
    for i in range(N):
        for j in range(M):
            if tmp_board[i][j]:
                bfs(i,j)
                # print(f"{z}년, tmp = {tmp_board}")
                flag +=1
                if flag > 1:
                    print(z)
                    exit()
print(0)
    
                