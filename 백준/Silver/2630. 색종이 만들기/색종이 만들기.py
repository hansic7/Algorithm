n = int(input())

board =[]
for _ in range(n):
    board.append(list(map(int, input().split())))

white = 0
blue = 0

def dfs(y, x, n):
    global white, blue
    num_check = board[y][x]
    for i in range(y, y+n):
        for j in range(x, x+n):
            if board[i][j] != num_check:
                    dfs(y, x , n//2)
                    dfs(y + n//2, x, n//2)
                    dfs(y, x +n//2 , n//2)
                    dfs(y+n//2, x+n//2 , n//2)
                    return
    if num_check == 0:
        white += 1
    else:
        blue += 1

dfs(0,0,n)
print(white)
print(blue)