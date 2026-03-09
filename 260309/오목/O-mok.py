board = [list(map(int, input().split())) for _ in range(19)]

def in_range(ny,nx):
    return 0 <= ny < 19 and 0 <= nx < 19

def hori(y,x):
    start_stone = board[y][x]
    
    for i in range(4):
        x += 1
        if not in_range(y,x) or not start_stone == board[y][x]:
            return 0,0,0
    return y,x-2,start_stone

def verti(y,x):
    start_stone = board[y][x]
    
    for i in range(4):
        y += 1
        if not in_range(y,x) or not start_stone == board[y][x]:
            return 0,0,0
    return y-2,x,start_stone

def diagonal_right(y,x):
    start_stone = board[y][x]
    
    for i in range(4):
        y,x = y+1, x+1
        if not in_range(y,x) or not start_stone == board[y][x]:
            return 0,0,0
    return y-2,x-2,start_stone

def diagonal_left(y,x):
    start_stone = board[y][x]
    
    for i in range(4):
        y,x = y+1, x-1
        if not in_range(y,x) or not start_stone == board[y][x]:
            return 0,0,0
    return y-2,x+2,start_stone

def solve():
    for y in range(19):
        for x in range(19):
            ny, nx, winner = hori(y,x)
            if winner: return ny + 1, nx + 1, winner
            
            ny, nx, winner = verti(y,x)
            if winner: return ny + 1,nx + 1, winner

            ny, nx, winner = diagonal_right(y,x)
            if winner: return ny + 1,nx + 1, winner

            ny, nx, winner = diagonal_left(y,x)
            if winner: return ny + 1,nx + 1, winner        
    return 0,0,0

y,x,winner = solve()
print(winner)
if winner:
    print(y, x)

# Please write your code here.


