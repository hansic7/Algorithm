N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

mapper = {'E':0, 'N':1, 'W':2, 'S':3}

def solve():
    dir_num = 0
    y,x = 0,0

    cnt = 0
    for i in range(N):
        dir_num = mapper[dir[i]]
        for _ in range(dist[i]):
            y, x = y + dy[dir_num] , x + dx[dir_num]
            cnt += 1
            if y == 0 and x == 0:
                print(cnt)
                return
    print(-1)



solve()
# Please write your code here.