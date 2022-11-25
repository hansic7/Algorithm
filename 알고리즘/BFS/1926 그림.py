from collections import deque

# N, M = map(int, input().split())
N , M = 6,5

board = []
# for _ in range(N):
#     board.append(list(map(int, input().split())))

d = ['1 1 0 1 1',
'0 1 1 0 0',
'0 0 0 0 0',
'1 0 1 1 1',
'0 0 1 1 1',
'0 0 1 1 1']

for i in range(6):
    board.append(list(map(int, d[i].split())))

visited = []
for i in range(N):
    visited.append([0]*M)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
how_big = [0]

def bfs(y,x):
    q = deque()
    q.append([y,x])
    visited[y][x] = 1
    tmp = 1

    while q:
        y, x = q.popleft()
        

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<M and not visited[ny][nx] and board[ny][nx] == 1:
                tmp += 1
                q.append([ny,nx])
                visited[ny][nx] = 1
                print(f"this is tmp in bfs = {tmp}")
    
    how_big.append(tmp)

cnt = 0
            
for j in range(N):
    for i in range(M):
        if board[j][i] == 1 and not visited[j][i]:
            bfs(j,i)
            cnt += 1
            

print(cnt)
print(max(how_big))
