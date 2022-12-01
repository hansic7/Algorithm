from collections import deque

ie = ['*****************',
'.............**$*',
'*B*A*P*C**X*Y*.X.',
'*y*x*a*p**$*$**$*',
'*****************']


# N = int(input())
N =1

entr = []

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

    