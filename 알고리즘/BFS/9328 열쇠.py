from collections import deque

ie = ['*****************',
'.............**$*',
'*B*A*P*C**X*Y*.X.',
'*y*x*a*p**$*$**$*',
'*****************']


# N = int(input())
N =1

entr = []

def bfs():
    q = deque()
    for i in entr:
        q.append(i)
        while q:
            y,x = q.popleft()
            for ny,nx in [(y+1, x), (y, x+1), (y-1, x), (y, x-1)]:
                if 0<=ny<h and 0<=nx and not visited[ny][nx]:
                    if map[ny][nx] == '.':
                        q.append([ny, nx])
                        visited[ny][nx] = True
                    elif map[ny][nx] != '*':
                        if map[ny][nx].islower():
                            key.append(map[ny][nx])
                            map[ny][nx] = '.'
                            q.append([ny,nx])
                        else:
                            if map[ny][nx].islower() in key:
                                q.append([ny,nx])
                        visited[ny][nx] = True

for _ in range(N):
    h , w = 5, 17
    # h, w = map(int, input().split())
    # map = [input().strip() for i in range(h)]
    map = [ie[i].strip() for i in range(h)]
    key= list(input().strip())
    
    ### 입구 저장
    for i in range(w):
        if map[0][i] != '*':
            entr.append([0,i])
        elif map[h-1][i] != '*':
            entr.append([h-1,i])
    for i in range(h):
        if map[i][0] != '*':
            entr.append([i,0])
        elif map[i][w-1] != '*':
            entr.append([i,w-1])

    ##두번 들어갈거임 키만 찾을수 있어서
    for _ in range(2):  
        visited = [[0]*w for i in range(h)]
        

