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
def bfs_edge(y,x,z):
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
                    board[ny][nx] = z
                elif board[ny][nx] == 0:
                    if [y,x] not in edge:
                        edge.append([y,x])
        # print(f"{board}")
        # print(edge)
        # print()
    return(edge)

edges = [0]
z = 1
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            z += 1
            edges.append(bfs_edge(i,j,z))

# bfs_edge(0,7,2)

print(f"{board}")
print()
print(f"edges = {edges}")

# [2, 2, 2, 0, 0, 0, 0, 3, 3, 3], 
# [2, 2, 2, 2, 0, 0, 0, 0, 3, 3], 
# [2, 0, 2, 2, 0, 0, 0, 0, 3, 3], 
# [0, 0, 2, 2, 2, 0, 0, 0, 0, 3], 
# [0, 0, 0, 2, 0, 0, 0, 0, 0, 3], 
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 3], 
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 4, 4, 0, 0, 0, 0], 
# [0, 0, 0, 0, 4, 4, 4, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]