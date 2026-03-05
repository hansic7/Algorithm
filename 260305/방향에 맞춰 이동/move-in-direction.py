n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
# dir = [move[0] for move in moves]
# dist = [int(move[1]) for move in moves]
dx, dy = [1, -1, 0, 0], [0, 0,-1, 1]
y,x = 0,0

def dir_to_num(dir):
    if dir == 'E':
        return 0
    elif dir == 'W':
        return 1
    elif dir == 'S':
        return 2
    elif dir == 'N':
        return 3

for dir, dist in moves:
    y = y + (dy[dir_to_num(dir)] * int(dist))
    x = x + (dx[dir_to_num(dir)] * int(dist))

print(x,y)
# Please write your code here.
