from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]




visited = [[False]*N for _ in range(N)]
def bfs(y,x):
    q = deque()
    q.append(y,x)
    edge = []
    while q:
        y, x = q.popleft()
        for ny,nx in [(y,x+1), (y,x-1), (y+1,x), (y-1, x)]:
            if 0<=ny<N and 0<=nx<N and not visited[ny][nx]:
                if board[ny][nx] == 0:
                    edge.append([ny,nx])
                    visited[ny][nx] = True
                    break
                else:
                    q.append([ny,nx])
                    visited[ny][nx] = True
    return(edge)

