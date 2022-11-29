from collections import deque

N = int(input())
# N = 1

def bfs():
    q = deque()
    for i in fire:
        q.append(i)
    q.append(start)
    while q:
        y, x, z = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<h and 0<=nx<w:
                if z == 1 and not fire_board[ny][nx] and not board[ny][nx] == '#':
                    fire_board[ny][nx] = 1
                    q.append([ny,nx,1])
                if z == 0 and not fire_board[ny][nx] and not board[ny][nx] == '#' and board[ny][nx] == '.':
                    board[ny][nx] = board[y][x] + 1
                    q.append([ny,nx,0])
                # print(f"fire board is {fire_board}") ########
                # print(f"orig boaed is {board}")
                # print()
                if z == 0 and (ny == h-1 or nx == w-1 or ny == 0 or nx == 0) and not board[ny][nx] == '#':
                    print(board[ny][nx]+1)
                    return
    print("IMPOSSIBLE")



for _ in range(N):
    w, h = map(int, input().split())
    # w, h = 7,6
    dy = [1,-1,0,0]                    
    dx = [0,0,1,-1]
    fire_board = [[0]* w for i in range(h)]
    board = [list(map(str, input().strip())) for i in range(h)]
    # print(board) ####
    fire = []
    for i in range(h):
        for j in range(w):
            if board[i][j] == '@':
                start = [i,j,0]
                board[i][j] = 0
            elif board[i][j] == '*':
                fire.append([i,j,1])
                fire_board[i][j] = 1
    bfs()
