n, t = map(int, input().split())
r, c, d = input().split()
y, x = int(r), int(c)

dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]

if d == 'U':
    dir = 0
elif d == 'R':
    dir = 1
elif d == 'D':
    dir = 2
elif d == 'L':
    dir = 3

for _ in range(t):
    if dir == 0 and y == 1:
        dir = 2
    elif dir == 1 and x == n:
        dir = 3
    elif dir == 2 and y == n:
        dir = 0
    elif dir == 3 and x == 1:
        dir = 1
    else:
        y,x = y+dy[dir], x+dx[dir]

print(y,x)

# Please write your code here.