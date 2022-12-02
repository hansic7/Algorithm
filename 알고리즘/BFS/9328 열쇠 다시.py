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

def bfs():
    visited = [[0]*(w+2)for i in range(h+2)]
    cnt = 0
    q = deque()
    q.append([0,0])
    while q:
        y,x = q.popleft()
        for ny,nx in [(y+1, x), (y, x+1), (y-1, x), (y, x-1)]:
            if 0<=ny<(h+1) and 0<=nx<(w+1) :
                if not visited[ny][nx]:
                    #빈칸인 경우
                    if map[ny][nx] == '.': 
                        q.append([ny, nx])
                        visited[ny][nx] = True

                #알파벳인 경우
                elif map[ny][nx].isalpha():
                    #키인 경우
                    if map[ny][nx].islower() and map[ny][nx] not in key:
                        key.append(map[ny][nx])
                        q = deque()
                        q.append([ny,nx])
                        visited = [[0]*(w+2)for i in range(h+2)]
                        visited[ny][nx] = True
                        map[ny][nx] = '.'
                    #자물쇠인 경우
                    else:
                        if map[ny][nx].lower() in key:
                            q.append([ny,nx])
                            visited[ny][nx] = True
                            map[ny][nx] = '.'

                #문서인 경우
                elif map[ny][nx] == '$':
                    cnt += 1
                    map[ny][nx] = '.'
                    visited[ny][nx] = True
    return cnt

N = 1
for _ in range(N):
    # h, w = map(int, input().split())
    h , w =  5,17 ####
    # key= list(input().strip())
    key = ['c', 'z']
    # map = [list(input().strip() for _ in range(h))]
    
    map = [list(["."]*(w+1))]
    for i in range(h):
        # row = input()
        row = ie[i]
        row = '.' + row + '.'
        map.append(list(row.strip()))
    map.append(["."]*(w+1))


    # map = [list(ie[i].strip()) for i in range(h)] 

    print(bfs())
    