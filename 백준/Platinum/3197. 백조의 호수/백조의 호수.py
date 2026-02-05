from collections import deque

direction = [(0,1), (0,-1), (1,0), (-1,0)]
# arr = [['.', 'L'], ['.', '.'], ['X', 'X'], ['X', 'X'], ['X', 'X'], ['X', 'X'], ['X', 'X'], ['X', 'X'], ['.', '.'], ['.', 'L']]
arr = []
water_q = deque()
swan_q = deque()

N, M = map(int, input().split())
# N,M = 10,2
water_visited = [[0]*M for _ in range(N)]
swan_visited = [[0]*M for _ in range(N)]

for i in range(N):
    arr.append(list(input()))
    for j in range(M):
        if arr[i][j] == 'L':
            swan_q.append([i,j])
            water_q.append([i,j])
            water_visited[i][j] = True
        elif arr[i][j] == '.':
            water_q.append([i,j])
            water_visited[i][j] = True

swan_visited[swan_q[0][0]][swan_q[0][1]] = True
target_y, target_x = swan_q.pop()

def melt():
    global water_q, arr
    next_water_q = deque()

    while water_q:
        y,x = water_q.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not water_visited[ny][nx]:
                if arr[ny][nx] == 'X':
                    water_visited[ny][nx] = True
                    next_water_q.append([ny,nx])
                    arr[ny][nx] = '.'
    water_q = next_water_q

def bfs():
    global swan_q
    next_swan_q = deque()

    while swan_q:
        y,x = swan_q.popleft()
        if y == target_y and x == target_x:
            return True
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not swan_visited[ny][nx]:
                swan_visited[ny][nx] = True
                if arr[ny][nx] == 'X':
                    next_swan_q.append([ny,nx])
                else:
                    swan_q.append([ny,nx])
    swan_q = next_swan_q
    return False

day = 0
while True:
    if bfs():
        print(day)
        break
    melt()
    day += 1