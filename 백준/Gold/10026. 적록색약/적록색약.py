from collections import deque

N = int(input())

graph = []

for i in range(N):
    graph.append(list(input()))


def bfs(y,x):
    que = deque()
    que.append([y,x])
    
    while que:
        y, x = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if -1 < nx < N and -1 < ny < N and not visited[ny][nx]:
                if graph[y][x] == graph [ny][nx]:
                    que.append([ny,nx])
                    visited[ny][nx] = True

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = []
cnt = 0
for _ in range(N):
    visited.append([False] * N)
for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            bfs(y,x)
            cnt += 1

for y in range(N):
    for x in range(N):
        if graph[y][x] == 'R':
            graph[y][x] = 'G'

visited = []
cnt2 = 0
for _ in range(N):
    visited.append([False] * N)
for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            bfs(y,x)
            cnt2 += 1

print(f"{cnt} {cnt2}")