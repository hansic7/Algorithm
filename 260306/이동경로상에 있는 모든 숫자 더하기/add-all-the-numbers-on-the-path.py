N, T = map(int, input().split())
str = input()
arr = [list(map(int, input().split())) for _ in range(N)]

dy =[-1,0,1,0]
dx =[0,1,0,-1]
dir = 0
y,x = N//2, N//2

res = arr[y][x]

def in_range(ny,nx):
    return 0 <= ny < N and 0 <= nx < N

for s in str:
    if s == 'R':
        dir = (dir + 1) % 4
    elif s == 'L':
        dir = (dir + 3) % 4
    else:
        ny, nx = y + dy[dir], x + dx[dir]
        if in_range(ny,nx):
            y,x = ny,nx
            res += arr[ny][nx]

print(res)

# Please write your code here.