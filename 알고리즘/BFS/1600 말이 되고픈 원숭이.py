from collections import deque

K = int(input())
W, H = map(int, input().split())
# K = 1
# W, H = 4,4

board = [list(map(int, input().split())) for _ in range(H)]
# board = [[0,0,0,0],
# [1,0,0,0],
# [0,0,1,0],
# [0,1,0,0]]
# board =[[0,0,1,1,0],[0,0,1,1,0] ]


# visited = []
# for i in range(H):
#     for j in range(W):
#         visited.append([0]*31) 
# 이거 잘못 만듬 고쳐야되는데 귀찮//  일단 냅둠

visited =[[[0]*31 for i in range(W)] for j in range(H)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
d1 = [-2, -1, 1, 2, 2, 1, -1, -2]
d2 = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs():
    global K
    q = deque()
    q.append([0,0,K]) #마지막에 0말고 K집어넣어야됨
    while q:
        y, x, z = q.popleft()
        if y == H-1 and x == W-1:  
            print(visited[y][x][z])
            exit() 

        if 0 < z:
            for i in range(8):
                ny = y + d1[i]
                nx = x + d2[i]
                if 0<=ny<H and 0<=nx<W:
                    if not board[ny][nx] and not visited[ny][nx][z-1]:  #이거 z-1 로 체크해줘야되는 이유는 총 N번의 무브중에 먼저 들어와서 돌던 말이 있을수 있음
                        visited[ny][nx][z+1] = visited[y][x][z] + 1
                        q.append([ny,nx, z+1])

        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<H and 0<=nx<W:
                if not board[ny][nx] and not visited[ny][nx][z]:
                        visited[ny][nx][z] = visited[y][x][z]+1
                        q.append([ny, nx, z])

    print(-1)

bfs()