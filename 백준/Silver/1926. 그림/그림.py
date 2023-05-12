from collections import deque
n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

dy = [-1,1,0,0]
dx = [0,0,1,-1]

cnt = 0
sizeArr = [0]

def bfs(y,x):
    q = deque()
    q.append([y,x])
    size = 1
    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= ny < n and 0 <= nx < m and arr[ny][nx] == 1):
                arr[ny][nx] = 2
                q.append([ny,nx])
                size += 1
    sizeArr.append(size)


for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            arr[i][j] = 2
            cnt += 1
            bfs(i,j)
            
print(cnt)
print(max(sizeArr))