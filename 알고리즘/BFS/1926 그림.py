from collections import deque

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

visited = []
for i in range(N):
    visited.append([0]*M)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
how_big = [0]

def bfs(y,x):
    q = deque()
    q.append(y,x)
    
    while q:
        y, x = q.popleft()
        tmp = 1

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<M and not visited[ny][nx]:
                tmp += 1
                q.append([ny,nx])
    
    how_big.append(tmp)

cnt = 0
            
for j in range(N):
    for i in range(M):
        if board[j][i] == 1:
            bfs(j,i)
            cnt += 1

print(cnt)
print(max(how_big))
