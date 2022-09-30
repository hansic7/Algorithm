from collections import deque

N, k = map(int, input().split())

s = deque()
answer = []

for i in range(1, N+1): 
    s.appendleft(i)

for i in range(N):
    s.rotate(k-1)
    answer.append(s.pop())

print('<' + str(answer)[1:-1]  + '>')