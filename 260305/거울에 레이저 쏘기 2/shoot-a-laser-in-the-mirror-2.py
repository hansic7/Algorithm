n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

mapper = {'D':0, 'L': 1, 'U':2, 'R':3}
dy = [1,0,-1,0]
dx = [0,-1,0,1]

curr_dir = 0
y, x = 0,0

if k//n == 0:
    x = k%n-1
    y = 0
    curr_dir = 0
elif k//n == 1:
    y = k%n-1
    x = n-1
    curr_dir = 1
elif k//n == 2:
    y = n-1
    x = n - 1 - k % n
    curr_dir = 2
else:
    y = n - 1 - k % n
    x = 0
    curr_dir = 3

def in_range(y,x):
    if 0 <= y < n and 0 <= x < n:
        return True
    return False


def mirror(y,x):
    global curr_dir
    if grid[y][x] == '\\':
        if curr_dir == mapper['U']:
            curr_dir = mapper['L']
        elif curr_dir == mapper['R']:
            curr_dir = mapper['D']
        elif curr_dir == mapper['L']:
            curr_dir = mapper['U']
        elif curr_dir == mapper['D']:
            curr_dir = mapper['R']
    elif grid[y][x] == '/':
        if curr_dir == mapper['R']:
            curr_dir = mapper['U']
        elif curr_dir == mapper['U']:
            curr_dir = mapper['R']
        elif curr_dir == mapper['L']:
            curr_dir = mapper['D']
        elif curr_dir == mapper['D']:
            curr_dir = mapper['L']
def move():
    global y,x,curr_dir
    y = y + dy[curr_dir]
    x = x + dx[curr_dir]

cnt = 0
while True:
    if not in_range(y,x):
        print(cnt)
        break
    mirror(y,x)
    move()
    cnt += 1

    
print(y,x)
# Please write your code here.