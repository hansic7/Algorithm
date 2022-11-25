from collections import deque

F, S, G, U, D = map(int,input().split())
# F, S, G, U, D = 10,1,10,2,1
visited =[0]*(F+1)
# print(visited)
button = [U,-D]
visited[S] = 1
# print(visited)

def bfs():
    q = deque()
    q.append(S)
    while q:
        now = q.popleft()
        if now == G:
            print(visited[now]-1)
            exit()
        for i in range(2):
            new = now + button[i]
            if 1<= new <= F and not visited[new]:
                visited[new] = visited[now]+1
                q.append(new)
                # print(visited)
    print("use the stairs")
bfs()