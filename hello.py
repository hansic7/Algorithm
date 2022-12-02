from collections import deque

N = int(input())
# N =1

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
                    if maps[ny][nx] == '.':
                        q.append([ny, nx])
                        visited[ny][nx] = True
                    elif maps[ny][nx].isalpha():
                        if maps[ny][nx].islower():
                            key.append(maps[ny][nx])
                            maps[ny][nx] = '.'
                            q.append([ny,nx])
                            visited = [[0]*w for _ in range(h)]
                            visited[ny][nx] = True
                        else:
                            if maps[ny][nx].lower() in key:
                                q.append([ny,nx])
                                visited[ny][nx] = True
                    elif maps[ny][nx] == '$':
                        cnt += 1
                        visited[ny][nx] = True
    return cnt

for _ in range(N):
    h, w = map(int, input().split())
    maps = [list(input().strip()) for i in range(h)]
    
    key= list(input().strip())
    # h , w = 5, 11  ####
    # maps = [list(ie[i].strip()) for i in range(h)] 
    # key = ['c' , 'z' ]
    # key = ['i','r','o','n','y']
    # key = [0]
    
    
    ### 입구 저장
#     print(maps) ###
    for i in range(w):
        if maps[0][i] != '*':
            entr.append([-1,i])
        elif maps[h-1][i] != '*':
            entr.append([h,i])
    for i in range(h):
        if maps[i][0] != '*':
            entr.append([i,-1])
        elif maps[i][w-1] != '*':
            entr.append([i,w])

    ##두번 들어갈거임 키만 찾을수 있어서
    
    visited = [[0]*w for _ in range(h)]
    print(bfs())
    