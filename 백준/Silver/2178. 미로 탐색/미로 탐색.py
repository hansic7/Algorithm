from collections import deque

M, N = map(int, input().split())

dy = [0,-1,0,1]
dx = [1,0,-1,0]

arr = [] 
for i in range(M):
    arr.append(list(map(int, input().strip())))

visited = [[0]*N for _ in range(M)] 

q = deque()
q.append([0,0])
visited[0][0] = 0

while q:
    y,x = q.popleft()

    if y == M-1 and x == N-1:
        print(visited[y][x]+1)
        exit()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if  0 <= ny < M and 0 <= nx < N and arr[ny][nx] == 1 and not visited[ny][nx]:
            q.append([ny,nx])
            visited[ny][nx] = visited[y][x]+1
    
print(-1)
