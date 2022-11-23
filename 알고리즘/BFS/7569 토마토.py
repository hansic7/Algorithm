from collections import deque
import sys

M, N, H = map(int,input().split())
board = []
q = deque()

for i in range(H):
    two_dimen = []
    for j in range(N):
        two_dimen.append(list(map(int, sys.stdin.readline().split())))
        for k in range(M):
            if two_dimen[j][k] == 1:
                q.append([i,j,k])
    board.append(two_dimen)

dx = [1, -1, 0, 0, 0, 0]
dy = [0,  0, 1,-1, 0, 0]
dz = [0,  0, 0, 0, 1, -1]

def bfs():
     while q: 
        x,y,z = q.popleft()
        for i in range(6):
            a = x+dx[i]
            b = y+dy[i]
            c = z+dz[i]
            if 0<=a<H and 0<=b<N and 0<=c<M and board[a][b][c] == 0:
                q.append([a,b,c])
                board[a][b][c] = board[x][y][z] + 1

bfs()
day = 0
for i in board:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()
        day = max(day, max(j))
print(day-1)