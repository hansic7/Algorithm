from collections import deque

N, M = map(int, input().split()) ###
board = [[[]for j in range(N+1)] for i in range(N+1)]
light_on = [[False]*(N+1) for i in range(N+1)]
visited = [[False]*(N+1) for i in range(N+1)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt = 1
q = deque()

for i in range(M):
    a,b,c,d, = map(int, input().split())
    board[a][b].append([c,d])

def turn_light(y,x):
    global cnt
    global visited
    global q
    for i,j in board[y][x]:
            if light_on[i][j] == False:
                light_on[i][j] = True
                cnt += 1
                visited = [[False]*(N+1) for i in range(N+1)]
                q = deque()
                q.append([1,1])
    board[y][x]=[]

def bfs():
    global q
    global cnt
    q.append([1,1])
    light_on[1][1] = True
    while q:
        y,x = q.popleft()
        turn_light(y,x)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 1<=ny<=N and 1<=nx<=N and light_on[ny][nx] == True and not visited[ny][nx]:
                q.append([ny,nx])
                visited[ny][nx] = True
    return (cnt)

print(bfs())