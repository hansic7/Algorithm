from collections import deque

M, N, K = map(int, input().split())

board = []

for i in range(M):
    board.append([0]*N)
    
for i in range(K):
    a,b,c,d = map(int, input().split())
    for i in range(b,d):
        for j in range(a,c):
            board[i][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
            
def bfs(y,x):
    q = deque()
    q.append([y,x])
    board[y][x] = 1
    
    tmp = 1
    while q:
        y, x = q.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=ny<M and 0<=nx<N and not board[ny][nx]:
                board[ny][nx] = 1
                q.append([ny,nx])
                tmp += 1
                
    size_count.append(tmp)



size_count =[]
empty_count = 0
for j in range(M):
    for i in range(N):
        if not board[j][i]:
            empty_count += 1
            bfs(j,i)
            
size_count.sort()
print(empty_count)
for i in size_count:
    print(i, end = ' ')