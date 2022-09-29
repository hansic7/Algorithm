from collections import deque

cnt = 0
N, n = map(int,input().split())
find = deque()

que = deque()
for i in range (1, N+1):
    que.append(i)
    
find.extend(map(int, input().split()))

for i in range(n):
    if (N/2)-0.5 >= que.index(find[i]):
        while find[i] != que[0]:
            que.rotate(-1)
            cnt += 1
    else:
        while find[i] != que[0]:
            que.rotate(1)
            cnt += 1
    if find[i] == que[0]:
        que.popleft()
    N -=1
print (cnt)