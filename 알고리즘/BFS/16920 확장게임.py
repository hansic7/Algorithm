from collections import deque

N, M, P = map(int, input().split())
move = list(map(int, input().split()))
board = [list(input().strip()) for _ in range(N)]

ply_str = [[] for i in range(P+1)]
for i in range(N):
    for j in range(M):
        if "1"<= board[i][j] <= str(P+1):
            board[i][j] = int(board[i][j])
            ply_str[int(board[i][j])].append([i,j,1])

where = [[] for i in range(P+1)]
            
def bfs(p):
    q1 = deque()
    q2 = deque()
    for i,j in where[p]:
        q1.append([i,j,0])
    where[p] = []
    
    for _ in range(move[p-1]):
        for ss in q1:
        y,x,z = q1.popleft()
        for ny, nx in range([(y+1, x), (y-1, x), (y,x+1), (y,x-1)]):
            if 0<=ny<N and 0<=nx<M and board[ny][nx] == '.':
                if z <= move[p]:
                    board[ny][nx] = p
                    q.append(ny)

        q1 = q2
        q1 = deque()