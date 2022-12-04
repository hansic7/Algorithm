from collections import deque
import copy

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
    edge = []
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
    return(edge)

edges = [0, 0]
z = 2  ##섬에 넘버 붙여줄거임 0은바다 1은 애초섬이니 2부터 레이블링 시작
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            edges.append(bfs_edge(i,j,z))
            z += 1

print(edges)
for i in edges[2]:
    cc = 0
    print(i)
    cc+=1

# 2부터 z까지 bfs 한번씩 다돌림
def bfs_bridge(z):
    # q = copy.deepcopy(edges[z]) ## q 그대로 가져오는거에서 문제생길수도?
    q = deque()  ## 대안
    for i in edges[z]:
        q.append(i)
    cnt = 1
    tmp_board = copy.deepcopy(board)
    while q:
        y,x = q.popleft()
        for ny,nx in [(y,x+1), (y,x-1), (y+1,x), (y-1, x)]:
            if 0<=ny<N and 0<=nx<N:
                if tmp_board[ny][nx] == 0:
                    tmp_board[ny][nx] = cnt
                    cnt += 1                    
                    q.append([ny,nx])
                elif tmp_board[ny][nx] != z:
                    return(cnt-1)
    return(cnt)

for i in range(2, z+1):
    res = 0
    res = min(res, bfs_bridge(i))

print(res)