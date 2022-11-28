from collections import deque

while True:
    L, C, R = map(int, input().split())
    if L == 0 and C == 0 and R == 0:
        exit()

    board = []
    for i in range(L):
        tmp = []
        for j in range(C):
            tmp.append(list(input().strip()))
        board.append(tmp)
        input() ## 입력값에 빈줄 하나가 더 들어온다 그래서 틀렸었음 ##

    for i in range(L):
        for j in range(C):
            for k in range(R):
                if board[i][j][k] == 'S':
                    start = [i,j,k]
                    board[i][j][k] = 0
                elif board[i][j][k] == 'E':
                    end = [i,j,k]

    dz = [1,-1,0,0,0,0]                    
    dx = [0,0,1,-1,0,0]
    dy = [0,0,0,0,-1,1]             

    def bfs():
        q = deque()
        q.append(start)
        while q:
            # print(f"this is que {q}")
            z, y, x = q.popleft()
            
            
            for i in range(6):
                nz = z + dz[i]
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nz<L and 0<=ny<C and 0<=nx<R:
                    if board[nz][ny][nx] == "." or board[nz][ny][nx] == "E" :
                        board[nz][ny][nx] = board[z][y][x] + 1
                        q.append([nz,ny,nx])
                        # print(f"{[nz,ny,nx]} and {board}")
                        # print()
                        if nz == end[0] and ny == end[1] and nx == end[2]:
                            print(f"Escaped in {board[nz][ny][nx]} minute(s).")
                            return
        print("Trapped!")

    bfs()
    