commands = input()

dy = [-1,0,1,0]
dx = [0,1,0,-1]

dir_num = 0
y,x = 0,0
cnt = 0
moved = False

for c in commands:
    if c == 'R':
        dir_num = (dir_num + 1) % 4
    elif c == 'L':
        dir_num = (dir_num + 3) % 4
    else:
        y = y + dy[dir_num]
        x = x + dx[dir_num]
        moved = True
    cnt += 1
    if y == 0 and x == 0 and moved:
        print(cnt)
        break

if not (y == 0 and x == 0 and moved):
    print(-1)
# Please write your code here.