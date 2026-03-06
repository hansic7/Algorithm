y, x = map(int, input().split())
arr = [list(input().split()) for _ in range(y)]

def solve():
    start_point = arr[0][0]
    res = 0
    for i in range(1, y-1):
        for j in range(1, x-1):
            if arr[i][j] != start_point:
                first_jump = arr[i][j]
                for k in range(i+1, y-1):
                    for l in range(j+1, x-1):
                        if arr[k][l] != first_jump:
                            res += 1
    return res
                            
if arr[0][0] == arr[y-1][x-1]:
    print(0)
else:
    print(solve())
# Please write your code here.