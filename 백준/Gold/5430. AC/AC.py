from collections import deque

N = int(input())

for i in range (N):
    todo = input()
    lens = int(input())
    queque = input()[1: -1].split(',')
    if lens == 0:
        que = []
    else:
        que = deque(queque)
    
    flag = 1
    n = len(todo)
    for i in range(n):
        if todo[i] == 'R':
            if flag:
                flag -= 1
            else:
                flag += 1
        else:
            if not que or que == 0:
                print ("error")
                break
            else:
                if flag:
                    que.popleft()
                else:
                    que.pop()    
    else:    
        if flag:
              print('[' + ",".join(que) + ']')
        else:
            que.reverse()
            print('[' + ",".join(que) + ']')