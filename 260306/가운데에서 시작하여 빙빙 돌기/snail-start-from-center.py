n = int(input())
grid = [[0] * n for _ in range(n)]

dy = [0,-1,0,1]
dx = [1,0,-1,0]

dir = 0
y,x = n//2, n//2

grid[y][x] = 1

def in_range(ny,nx):
    return 0 <= ny < n and 0 <= nx < n

if n != 1:
    x +=1
    grid[y][x] = 2

for _ in range(n*n-2):
    
    next_dir = (dir + 1) % 4
    ny, nx = y + dy[next_dir], x + dx[next_dir]

    if in_range(ny,nx) and grid[ny][nx] != 0:
        ny, nx = y + dy[dir], x + dx[dir]
    elif in_range(ny,nx) and grid[ny][nx] == 0:
        dir = next_dir
    
    grid[ny][nx] = grid[y][x] + 1
    y,x = ny,nx

for i in range(n):
    for j in range(n):
        print(grid[i][j], end = ' ')
    print()

