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
 
# N = int(input())  ####
# board = [list(map(int, input().split())) for _ in range(N)]

N = 10
board= [list(map(int, dd[i].split())) for i in range(N)] ###


visited = [[False]*N for _ in range(N)]
def bfs_edge(y,x,z):
    q = deque()
    q.append([y,x])
    # edge = []
    while q:
        y, x = q.popleft()
        for ny,nx in [(y,x+1), (y,x-1), (y+1,x), (y-1, x)]:
            if 0<=ny<N and 0<=nx<N and not visited[ny][nx]:
                if board[ny][nx] == 1:
                    q.append([ny,nx])
                    visited[ny][nx] = True
                    board[ny][nx] = z
                # elif board[ny][nx] == 0:
                #     if [y,x] not in edge:
                #         edge.append([y,x])
    # return(edge)

# edges = [0, 0]
z = 2  ##섬에 넘버 붙여줄거임 0은바다 1은 애초섬이니 2부터 레이블링 시작
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            # edges.append(bfs_edge(i,j,z))
            bfs_edge(i,j,z)
            z += 1


# 2부터 z까지 bfs 한번씩 다돌림
def bfs_bridge(z):    #########!!!!!!가장 중요한것은 이동 횟수를 visited에다가 찍음 !!!!###
                        ### 혹은 while문 안에서 이동횟수를 세번째 인자로 depth 처럼 받아줄수도 있음 ###
    # q = copy.deepcopy(edges[z]) ## q 그대로 가져오는거에서 문제생길수도?
    q = deque()  ## 대안
    check = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if 0<=i<N and 0<=j<N and board[i][j] == z:
                q.append([i, j])
    ## che
                
    while q:
        y,x = q.popleft()
        for ny,nx in [(y,x+1), (y,x-1), (y+1,x), (y-1, x)]:
            if 0<=ny<N and 0<=nx<N:
                ## 종료조건 : 보드 번호 0보다크고 // 지금 섬이 아닐때
                if 0 < board[ny][nx] and z != board[ny][nx]:
                    print(f"y,x = {y},{x} and ny,nx = {ny},{nx}")
                    for i in check:
                        print(i)
                    print()
                    return(check[y][x])
                
                ### 이동횟수 체크 : 바다고 // 방문안했을때 -> 방문배열에 이동횟수 체크
                if 0 == board[ny][nx] and check[ny][nx] == 0:
                    check[ny][nx] = check[y][x] + 1
                    q.append([ny,nx])
    return (0)

for i in board:
    print(i)
print()

res = 2000 * 2000
for i in range(2, z):
    res = min(res, bfs_bridge(i))

print(res)