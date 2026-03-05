n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
y,x = 0, 0
curr_dir = 0

arr[y][x] = 'A'

def in_range(ny,nx):
    return 0 <= ny < n and 0 <= nx < m and arr[ny][nx] == 0

for i in range(n * m - 1):
    ny, nx = y + dy[curr_dir], x + dx[curr_dir]
    if not in_range(ny,nx):
        curr_dir = (curr_dir + 1) % 4
        ny, nx = y + dy[curr_dir], x + dx[curr_dir]
    if arr[y][x] == 'Z':
        arr[ny][nx] = 'A'
    else:
        arr[ny][nx] = chr(ord(arr[y][x]) + 1)
    y,x = ny,nx
    
for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()
# Please write your code here.
