from collections import deque

dd = ['1 1 1 0 0 0 0 1 1 1',
'1 1 1 1 0 0 0 0 1 1',
'1 0 1 1 0 0 0 0 1 1',
'0 0 1 1 1 0 0 0 0 1',
'0 0 0 1 0 0 0 0 0 1',
'0 0 0 0 0 0 0 0 0 1',
'0 0 0 0 0 0 0 0 0 0',
'0 0 0 0 1 1 0 0 0 0',
'0 0 0 0 1 1 1 0 0 0',
'0 0 0 0 0 0 0 0 0 0']

# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]

N = 10
board= [list(map(int, dd[i].split())) for i in range(N)] ###


visited = [[False]*N for _ in range(N)]
def bfs_edge(y,x):
    q = deque()
    q.append([y,x])
    edge = deque()
    while q:
        y, x = q.popleft()
        for ny,nx in [(y,x+1), (y,x-1), (y+1,x), (y-1, x)]:
            if 0<=ny<N and 0<=nx<N and not visited[ny][nx]:
                if board[ny][nx] == 1:
                    q.append([ny,nx])
                    visited[ny][nx] = True
                else:
                    if [ny,nx] not in edge:
                        edge.append([ny,nx])
    return(edge)

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            