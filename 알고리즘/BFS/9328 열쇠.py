from collections import deque

ie = ['*****************',
'.............**$*',
'*B*A*P*C**X*Y*.X.',
'*y*x*a*p**$*$**$*',
'*****************']

# ie = ['*ABCDE*',
# 'X.....F',
# 'W.$$$.G',
# 'V.$$$.H',
# 'U.$$$.J',
# 'T.....K',
# '*SQPML*']

# ie =['*.*********',
# '*...*...*x*',
# '*X*.*.*.*.*',
# '*$*...*...*',
# '***********']


# N = int(input())
N = 1

entr = []

def bfs():
    global visited
    cnt = 0
    q = deque()
    for i in entr:
        q.append(i)
        while q:
            y,x = q.popleft()
            for ny,nx in [(y+1, x), (y, x+1), (y-1, x), (y, x-1)]:
                if 0<=ny<h and 0<=nx<w and not visited[ny][nx]:
                    if map[ny][nx] == '.':
                        q.append([ny, nx])
                        visited[ny][nx] = True
                    elif map[ny][nx].isalpha():
                        if map[ny][nx].islower():
                            key.append(map[ny][nx])
                            map[ny][nx] = '.'
                            q.append([ny,nx])
                            visited = [[0]*w for _ in range(h)]
                            visited[ny][nx] = True
                        else:
                            if map[ny][nx].lower() in key:
                                q.append([ny,nx])
                                visited[ny][nx] = True
                    elif map[ny][nx] == '$':
                        cnt += 1
                        visited[ny][nx] = True
    return cnt

for _ in range(N):
    # h, w = map(int, input().split())
    h , w =   5,17####
    # map = [list(input().strip() for _ in range(h))]
    # key= list(input().strip())
    
    map = [list(ie[i].strip()) for i in range(h)] 
    key = ['c' , 'z' ]
    # key = ['i','r','o','n','y']
    # key = [0]
    
    
    ### 입구 저장
    for i in range(w):
        if map[0][i] != '*':
            entr.append([-1,i])
        elif map[h-1][i] != '*':
            entr.append([h,i])
    for i in range(h):
        if map[i][0] != '*':
            entr.append([i,-1])
        elif map[i][w-1] != '*':
            entr.append([i,w])
    
    visited = [[0]*w for i in range(h)]
    print(bfs())
    

