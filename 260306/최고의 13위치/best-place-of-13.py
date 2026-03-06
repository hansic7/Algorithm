n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

res = 0
for i in range(n):
    for j in range(n-2):
        tmp = 0
        tmp = grid[i][j] + grid[i][j + 1] + grid[i][j +2]
        res = max(res, tmp)

print(res)
    


# Please write your code here.