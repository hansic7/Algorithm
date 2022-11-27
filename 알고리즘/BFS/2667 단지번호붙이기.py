from collections import deque

# N = int(input())
# board = [list(map(int, input().strip())) for i in range(N)]

N = 7
dd = ['0110100',
'0110101',
'1110101',
'0000111',
'0100000',
'0111110',
'0111000']
board = []
for i in range(N):
    board.append(list(map(int, dd[i].strip())))


dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(i, j):
    q = deque()
    q.append([i,j])
    board[i][j] = 2
    cntr = 1
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<N and board[ny][nx]==1:
                cntr +=1
                q.append([ny,nx])
                board[ny][nx] = 2
    return (cntr)

cnt = 0
danji =[]
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            cnt += 1
            # a =bfs(i,j)
            danji.append(bfs(i,j))

danji.sort()
print(cnt)
for i in danji:
     print(i)