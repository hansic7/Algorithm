from collections import deque

# M, N, K = map(int, input().split())
M, N, K = 5,7,3

board = []

dd = ['0 2 4 4',
'1 1 2 5',
'4 0 6 2']

for i in range(M):
    board.append([0]*N)

for i in range(3):
    a,b,c,d = map(int, dd[i].split())
    for i in range(b,d):
        for j in range(a,c):
            board[i][j] = 1
    
for i in range(K):
    a,b,c,d = map(int, input().split())
    for i in range(b,d):
        for j in range(a,c):
            board[i][j] = 1

print(f"current board = {board}\n" )

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
    print(f"current board in bfs= {board}")
    print(f"tmp is = {tmp}")       
    print('')


size_count =[]
empty_count = 0
for j in range(M):
    for i in range(N):
        if not board[j][i]:
            empty_count += 1
            bfs(j,i)
            
size_count.sort()
print(empty_count)
print(size_count)
for i in size_count:
    print(i, end = ' ')