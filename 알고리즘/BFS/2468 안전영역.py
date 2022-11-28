from collections import deque
import copy

# N = 5
# dd =['6 8 2 6 2',
# '3 2 3 4 6',
# '6 7 3 3 2',
# '7 2 5 3 6',
# '8 9 5 2 7']
# N = 7 
# dd = ['9 9 9 9 9 9 9',
# '9 2 1 2 1 2 9',
# '9 1 8 7 8 1 9',
# '9 2 7 9 7 2 9',
# '9 1 8 7 8 1 9',
# '9 2 1 2 1 2 9',
# '9 9 9 9 9 9 9']
# board = [list(map(int, dd[i].split())) for i in range(N)]


N = int(input())
board = [list(map(int, input().split())) for i in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(i,j):
    q = deque()
    q.append([i,j])
    tmp_board[i][j] = 0
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<N and tmp_board[ny][nx]:
                q.append([ny,nx])
                tmp_board[ny][nx] = 0

high = 0
for i in range(N):
    tmp = max(board[i])
    high = max(high, tmp)

result = 0
for z in range(high):
    tmp_board  = copy.deepcopy(board)
    cnt = 0
    
    for i in range(N):
        for j in range(N):
            if tmp_board[i][j] <= z:
                tmp_board[i][j] = 0

    for i in range(N):
        for j in range(N):
            if tmp_board[i][j]:
                bfs(i,j)
                cnt += 1

    if result < cnt:
        result = cnt

print(result)