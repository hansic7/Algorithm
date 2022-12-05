import sys
from collections import deque

imput = sys.stdin.readline


dd = ['1 1 1 0 0 0 0 1 1 1',
'1 1 1 1 0 0 0 0 1 1',
'1 0 1 1 0 0 0 0 1 1',
'0 0 1 1 1 0 0 0 0 1',
'0 0 0 1 0 0 0 0 0 1',
'0 0 0 0 0 0 0 0 0 1',
'0 0 0 0 0 0 0 0 0 0',
'0 0 0 0 1 1 0 0 0 0',
'0 0 0 0 1 1 1 0 0 0',
'0 0 0 0 0 0 0 0 0 0']

# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]

# n = 10
# board= [list(map(int, dd[i].split())) for i in range(N)] ###

# n = int(input())
# graph = [list(map(int, dd[i].split())) for i in range(n)]
# visited = [[False] * n for _ in range(n)]

# dir = ((0, 1), (0, -1), (1, 0), (-1, 0))

# def condition(ni, nj):
#     return ni < 0 or ni >= n or nj < 0 or nj >= n or visited[ni][nj]

# def marking(y, x, mark):
#     q = deque()
#     q.append((y, x))
#     graph[y][x] = mark
#     visited[y][x] = True
#     while q:
#         i, j = q.popleft()
#         for dy, dx in dir:
#             ni, nj = i + dy, j + dx
#             if condition(ni, nj) or not graph[ni][nj]:   continue
#             graph[ni][nj] = mark
#             visited[ni][nj] = True
#             q.append((ni, nj))

# def getDist(y, x, now):
#     q = deque()
#     q.append((y, x, 0))
#     while q:
#         i, j, cnt = q.popleft()
#         if graph[i][j] != 0 and graph[i][j] != now:
#             for i in graph:
#                 print(i)
#             print()
#             return cnt
#         for dy, dx in dir:         ###큐에 닮을때 원래 그래프에 찍힐 이동거리를 3번째 인자로 넘겨줌
#             ni, nj = i + dy, j + dx
#             if condition(ni, nj) or graph[ni][nj] == now:   continue
#             visited[ni][nj] = True
#             q.append((ni, nj, cnt + 1))
#     return 2000
            

# mark = 1
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] and not visited[i][j]:
#             marking(i, j, mark)
#             mark += 1

            
# ans = 2000
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] != 0:
#             visited = [[False] * n for _ in range(n)]
#             ans = min(ans, getDist(i, j, graph[i][j]))
            
        
# print(ans - 1)


###################################################################################################################################
################################################################################################################################
###########################################################################################################################


import sys
from collections import deque
sys.setrecursionlimit(10**6)

num = 10
arr = [list(map(int, dd[i].split())) for i in range(num)]
# num = int(input())
# arr = [list(map(int,input().split())) for _ in range(num)]

ans = sys.maxsize

def dfs(i,j):
    global cnt
    if i < 0 or i >= num or j < 0 or j >= num:
        return False
    if arr[i][j] == 1:
        arr[i][j] = cnt
        for x,y in (0,1),(0,-1),(1,0),(-1,0):
            nx = x+i
            ny = y+j
            dfs(nx,ny)
        return True

def bfs(n):
    global ans
    check = [[-1] * num for _ in range(num)]
    q = deque()

    for i in range(num):
        for j in range(num):
            if arr[i][j] == n:
                q.append((i,j))
                check[i][j] = 0
    while q:
        x,y = q.popleft()
        for a,b in (0,-1),(0,1),(1,0),(-1,0):
            nx = x+a
            ny = y+b
            if nx < 0 or nx >= num or ny < 0 or ny >= num:
                continue
            #다른 섬에 도착한 경우
            if arr[nx][ny] > 0 and arr[nx][ny] != n:
                ans = min(ans,check[x][y])
                return
            #바다이고, 방문한 적이 없다면
            if arr[nx][ny] == 0 and check[nx][ny] == -1:
                check[nx][ny] = check[x][y]+1
                q.append((nx,ny))


cnt = 2
for i in range(num):
    for j in range(num):
        if dfs(i,j) == True:
            cnt+=1

for i in arr:
    print(i)

for i in range(2,cnt):
    bfs(i)



print(ans)