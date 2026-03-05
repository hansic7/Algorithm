n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

arr = [[0]*n for _ in range(n)]

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def comfort(y,x):
    cnt = 0
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] == 1:
            cnt += 1
    if cnt == 3:
        return True
    return False

for y,x in points:
    y,x = y-1,x-1

    arr[y][x] = 1
    if comfort(y,x):
        print(1)
    else:
        print(0)
    

# Please write your code here.