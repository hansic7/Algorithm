from collections import deque
N = int(input())
arr = [list(input().strip()) for _ in range(N)]



dy = [0,0,-1,1]
dx = [1,-1,0,0]

def bfs(y,x):
    q = deque()
    q.append([y,x])
    visited[y][x] = 1
    
    while q:
        y,x = q.popleft()

        for i in range(4):
          ny = y + dy[i]
          nx = x + dx[i]

          if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == arr[y][x] and not visited[ny][nx]:
              visited[ny][nx] = 1
              q.append([ny,nx])

# 적록색약 아닌 사람
notrg = 0
visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j)
            notrg += 1

# 적색으로 올 전환
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'
rg = 0
visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j)
            rg += 1

print(notrg,rg)
