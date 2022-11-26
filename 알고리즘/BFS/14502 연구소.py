from collections import deque
import copy

N, M = map(int, input().split())
# N, M = 7,7

board = []
virus = []
wall_cnt = 0
virus_cnt = 0
# dd = ['0 0 0 0 0 0',
# '1 0 0 0 0 2',
# '1 1 1 0 0 2',
# '0 0 0 0 0 2']

# dd = ['2 0 0 0 1 1 0',
# '0 0 1 0 1 2 0',
# '0 1 1 0 1 0 0',
# '0 1 0 0 0 0 0',
# '0 0 0 0 0 1 1',
# '0 1 0 0 0 0 0',
# '0 1 0 0 0 0 0']
for i in range(N):
    board.append(list(map(int, input().split())))
    # board.append(list(map(int, dd[i].split())))    
    for j in range(M):
        if board[i][j] == 2:
            virus.append([i, j])
            virus_cnt += 1
        elif board[i][j] == 1:
            wall_cnt += 1
            
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]         
result = N*M

def bfs():
    global result
    tmp_visited = copy.deepcopy(board)
    tmp_result = 0
    q = deque()

    for i in virus:
        q.append(i)
        
    while q:
        y,x = q.popleft()
    
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<M and tmp_visited[ny][nx] == 0:
                tmp_visited[ny][nx] = 1
                tmp_result += 1
                q.append([ny,nx])

    result = max(tmp_result, result)
    
            
def dfs(wall):
    if wall == 3:
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if not board[i][j]:
                board[i][j] = 1
                dfs(wall+1)
                board[i][j] = 0

dfs(0)
a = (M*N)-virus_cnt-result-wall_cnt-3
if a>0:
    print(a)
else:
    print(0)