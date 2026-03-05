n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]


y,x = 0,0


dy = [0,1,0,-1]
dx = [1,0,-1,0]
cur_dir = 0
arr[y][x] = 1

def in_range(y,x):
    return 0 <= y < n and 0 <= x < m and arr[y][x] == 0

for _ in range(n*m - 1):
    
    ny, nx = y + dy[cur_dir], x + dx[cur_dir]

    if not in_range(ny,nx):
        cur_dir = (cur_dir + 1) % 4
        ny, nx = y + dy[cur_dir], x + dx[cur_dir]
        
    arr[ny][nx] = arr[y][x] + 1
    y,x = ny,nx
    
for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()


# Please write your code here.