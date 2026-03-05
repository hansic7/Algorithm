dirs = input()

cur_dir = 0
x,y = 0,0
dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]

for dir in dirs:
    if dir == 'L':
        cur_dir = (cur_dir - 1 + 4) % 4
    elif dir == 'R':
        cur_dir = (cur_dir + 1 + 4) % 4    
    else:
        y,x = y + dy[cur_dir], x + dx[cur_dir]

print(x,y)
# Please write your code here.