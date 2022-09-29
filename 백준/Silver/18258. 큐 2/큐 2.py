import sys
from collections import deque

que = deque()
N = int(sys.stdin.readline())
for _ in range(N) :
    i = sys.stdin.readline().split()

    if i[0] == 'push':
        que.append(int(i[1]))

    elif i[0] == 'pop':
        if que:
            print(que[0])
            que.popleft()
        else :
            print(-1)

    elif i[0] == 'size':
        print(len(que))

    elif i[0] == 'empty':
        if que:
            print (0)
        else :
            print (1)
            
    elif i[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
            
    elif i[0] == 'back':
        if que:
            print(que[-1])   
        else:
            print(-1)