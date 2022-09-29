from collections import deque

N = int(input())
answer =deque()


for i in range(1, N+1):
    answer.append(i)

for i in range(N-1):
    answer.popleft ()
    answer.rotate(-1)

print(answer[0])