from collections import deque

K = int(input())

for _ in range(K):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    q = deque(arr)
    idxQ = deque()
    for i in range(n):
        idxQ.append(0)
    idxQ[m] = 1

    cnt = 0
    while 1:
        pri = max(q)
        if q[0] == pri:
            cnt += 1
            if idxQ[0] == 1:
                print(cnt)
                break
            else:
                q.popleft()
                idxQ.popleft()
        else:
            q.rotate(-1)
            idxQ.rotate(-1)
