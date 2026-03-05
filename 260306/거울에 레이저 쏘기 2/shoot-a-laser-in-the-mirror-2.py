n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input()) - 1

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def start_point():
    y,x,dir_num = 0,0,0

    if k // n == 0:
        y = 0
        x = k % n
        dir_num = 1
    elif k // n == 1:
        x = n -1
        y = k % n
        dir_num = 2
    elif k // n == 2:
        y = n -1
        x = k % n
        dir_num = 0
    elif k // n == 3:
        x = 0
        y = k % n
        dir_num = 3

    return y,x, dir_num

def in_range(y,x):
    return 0 <= y < n  and 0 <= x < n

def mirror(y,x,dir_num):
    if grid[y][x] == '/':
        if dir_num == 0:
            return 3
        elif dir_num == 1:
            return 2
        elif dir_num == 2:
            return 1
        elif dir_num == 3:
            return 0
    else: 
        if dir_num == 0:
            return 1
        elif dir_num == 1:
            return 0
        elif dir_num == 2:
            return 3
        elif dir_num == 3:
            return 2

y, x, dir_num = start_point()
cnt = 0

while True:
    dir_num = mirror(y,x,dir_num)
    cnt += 1
    y, x = y + dy[dir_num], x + dx[dir_num]
    if not in_range(y,x):
        print(cnt)
        break