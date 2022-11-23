from collections import deque
import sys

board = []
N, M = map(int, input().split())
for i in range(N):
    board.append(list(map(int, input().strip())))

visited = []
for i in range(N):
    tmp = []
    for j in range(M):
        tmp.append([0]*2)
    visited.append(tmp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append([0,0,0])

    while q:
        y, x, z = q.popleft()
        
        if y == (N-1) and x == (M-1):
            print(visited[y][x][z]+1)
            exit()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N :
                if board[ny][nx] == 1 and z == 0:
                    visited[ny][nx][1] = visited[y][x][0]+1
                    q.append([ny,nx,1])

                elif board[ny][nx] == 0 and visited[ny][nx][z] == 0:
                    visited[ny][nx][z] = visited[y][x][z]+1
                    q.append([ny,nx,z])
    print(-1)

bfs()
            
