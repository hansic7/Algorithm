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

def bfs_edge(y,x):
    q = deque()
    q.append([y,x])
    edge = []
    while q:
        y, x = q.popleft()
        for ny,nx in [(y,x+1), (y,x-1), (y+1,x), (y-1, x)]:
            if 0<=ny<N and 0<=nx<N and not visited[ny][nx]:
                if board[ny][nx] == 1:
                    q.append([ny,nx])
                    visited[ny][nx] = 1
                elif board[ny][nx] == 0:
                    if [y,x] not in edge:
                        edge.append([y,x])
    return(edge)

#2부터 z까지 bfs 한번씩 다돌림
def bfs_bridge():
    # q = copy.deepcopy(edges[z]) ## q 그대로 가져오는거에서 문제생길수도?
    q = deque()  ## 대안
    tmp_board = copy.deepcopy(board)
    for [i,j] in edges:  ## for i 문 쓸때 그 배열에 있는거 모양 그대로 가져다 써야됨 걍 i,j로 가져오면 안됨
        q.append([i,j])
        # tmp_board[i][j] = z+1
    while q:
        y,x = q.popleft()
        for ny,nx in [(y,x+1), (y,x-1), (y+1,x), (y-1, x)]:
            if 0<=ny<N and 0<=nx<N:
                if tmp_board[ny][nx] == 1 and visited[ny][nx]:
                    continue
                elif tmp_board[ny][nx] == 0:
                    tmp_board[ny][nx] = tmp_board[y][x] + 1
                    visited[ny][nx] = 1
                    q.append([ny,nx])
                if tmp_board[ny][nx] == 1 and not visited[ny][nx]:
                    print("tmp visited")
                    for i in visited:
                        print(i)
                    print(f"exit y,x = {y}, {x} and ny,nx = {ny}, {nx} ")
                    for i in tmp_board:
                        print(i)
                    print()
                    return(tmp_board[y][x] - 1)
    print("tmp visited")
    for i in visited:
        print(i)
    print()
    for i in tmp_board:
        print(i)
    print()
    return(-1)

## int(main)
res = 1000 ** 2
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            visited = [[0]*N for _ in range(N)]
            edges = bfs_edge(i,j)
            res = min(res, bfs_bridge())
print(res)