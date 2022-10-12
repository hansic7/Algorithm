N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

minus_one = 0
zero = 0
one = 0

def dfs(y, x, n):
    global minus_one, zero, one

    num_check = board[y][x]
    for i in range(y, y + n):
        for j in range(x, x+n):
            if num_check != board[i][j]:
                #k, l 3인 이유는 9등분으로 쪼개야되니까 3*3칸 만드는 거임
                for k in range(3):  
                    for l in range(3):
                        dfs(y+k*n//3, x+l*n//3 , n//3)
                return
    if num_check==0:
        zero+=1
    elif num_check==1:
        one+=1
    elif num_check==-1:
        minus_one+=1
    return

dfs(0,0,N)

print(minus_one)
print(zero)
print(one) 