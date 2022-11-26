from collections import deque
import copy

dd = ['0 0 0 0 0 0',
'1 0 0 0 0 2',
'1 1 1 0 0 2',
'0 0 0 0 0 2']

N, M = 4,6

# N, M = map(int, input().split())
board = []
virus = []
wall = []
result = 0
for i in range(N):
    # board.append(list(map(int, input().split())))
    board.append(list(map(int, dd[i].split())))
    for j in range(M):
        if board[i][j] == 2:
            virus.append([i,j])
        elif board[i][j] == 1:
            wall.append([i,j])

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs():
    global result
    tmp = copy.deepcopy(board)
    q = deque()
    for i in virus:
        q.append(i)
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if 0<=ny<N and 0<=nx<M and tmp[ny][nx] == 0:
                tmp[ny][nx] = 2
                q.append([ny,nx])
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 0:
                cnt += 1
    result = max(result, cnt)

def dfs(wall):
    if wall == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                dfs(wall+1)
                board[i][j] = 0

dfs(0)
print(result)