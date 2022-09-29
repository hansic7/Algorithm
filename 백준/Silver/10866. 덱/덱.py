from collections import deque
import sys

N = int(input())

que = deque()

for i in range(N):
    a = sys.stdin.readline().split()
    
    if a[0] == 'push_front':
        que.appendleft(int(a[1]))
    
    elif a[0] == 'push_back':
        que.append(int(a[1]))
    
    elif a[0] == 'pop_front':
        if que:
            print(que.popleft())
        else: 
            print(-1)
            
    elif a[0] == 'pop_back':
        if que:
            print(que.pop())
        else: 
            print(-1)
    
    elif a[0] == 'size':
        print(len(que))
        
    elif a[0] == 'empty':
        if que:
            print (0)
        else:
            print (1)
            
    elif a[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
            
    elif a[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)