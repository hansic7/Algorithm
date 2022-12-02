from collections import deque

d = [(-1, 0), (1, 0), (0, 1), (0, -1)]

# ie = ['*****************',
# '.............**$*',
# '*B*A*P*C**X*Y*.X.',
# '*y*x*a*p**$*$**$*',
# '*****************']

# ie = ['*ABCDE*',
# 'X.....F',
# 'W.$$$.G',
# 'V.$$$.H',
# 'U.$$$.J',
# 'T.....K',
# '*SQPML*']

ie =['*.*********',
'*...*...*x*',
'*X*.*.*.*.*',
'*$*...*...*',
'***********']

def unlock():
    for i in range(h+2):
        for j in range(w+2):
            if map[i][j].lower() in key:
                map[i][j] = '.'
    key.clear()


def bfs():
    global key
    global cnt
    visited = [[0]*(w+2) for i in range(h+2)]
    q = deque()
    q.append([0,0])
    while q:
        y,x = q.popleft()
        for ii in range(4):
            ny = y + d[ii][0]
            nx = x + d[ii][1]
            if 0<=ny<(h+2) and 0<=nx<(w+2) and not visited[ny][nx]:
                
                #빈칸인 경우
                if map[ny][nx] == '*': 
                    continue
                    
                #알파벳인 경우
                if map[ny][nx].isupper():
                    continue
                if map[ny][nx].islower():
                    key.append(map[ny][nx]) 

                #문서인 경우
                if map[ny][nx] == '$':
                    cnt += 1
                map[ny][nx] = '.'  
                q.append([ny, nx])
                visited[ny][nx] = 1


# N = 1
# # N = int(input())
# for _ in range(N):
#     # h, w = map(int, input().split())
#     h , w =  5,11 ##5##
#     # key= list(input().strip())
#     # key = ['c', 'z']
#     key = [0]
#     cnt = 0
    
#     map = [list(["."]*(w+2))]
#     for i in range(h):
#         # row = input()
#         row = ie[i]
#         row = '.' + row + '.'
#         map.append(list(row.strip()))
#     map.append(["."]*(w+2))
#     while key:
#         unlock()
#         bfs()
#     print(cnt)
                
N = int(input())
for _ in range(N):
    h, w = map(int, input().split())
    cnt = 0
    
    map = [list(["."]*(w+2))]
    for i in range(h):
        row = input()
        row = '.' + row + '.'
        map.append(list(row.strip()))
    map.append(["."]*(w+2))
    
    key= list(input().strip())
    while key:
        unlock()
        bfs()
    print(cnt)
    