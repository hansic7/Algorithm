from collections import deque

t = int(input())

for _ in range(t):
    n, m, b = map(int, input().split())
    cnt = 0
    dy = [0, -1, 0, 1]
    dx = [1, 0, -1, 0]

    q = deque()
    visited = [[0]*n for _ in range(m)]
    arr = [[0]*n for _ in range(m)]

    for _ in range(b):
        x, y = map(int, input().split())
        arr[y][x] = 1

    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1 and not visited[i][j]:
                q.append([i, j])
                visited[i][j] = 1
                while q:
                    y, x = q.popleft()
                    for dir in range(4):
                        ny = y + dy[dir]
                        nx = x + dx[dir]
                        if 0 <= ny < m and 0 <= nx < n:
                            if arr[ny][nx] and not visited[ny][nx]:
                                q.append([ny, nx])
                                visited[ny][nx] = 1
                cnt += 1

    print(cnt)