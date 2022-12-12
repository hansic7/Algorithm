

#### 아래에 먼저 저장하는 식으로 하면, 예를 들어)
# 7
# 3 8
# 8 1 0
##  810에서 문제가 생김.
## 한번 연산한후 10 15 에서 10이 먼저 들어가 810을 18 11 0으로 바꿈
## 그후에 11은 또 호출이 되는데 그러면 미리 겹치는 1을 tmp에 저장해줘야됨
## 아니면 15+11로 오류가 생김
## ### 해결 방법은 밑에 쪽에서 위에 수를 가져와서 그 두개중max로 바꾸는거임


dd = ['7',
'3 8',
'8 1 0',
'2 7 4 4',
'4 5 2 6 5']
n= 5
import math
import time

start = time.time()
math.factorial(100000)



board = []
dp = []
# n = int(input()) ##
for i in range(n):
    # board.append(list(map(int, input().split()))) ##
    board.append(list(map(int, dd[i].split())))

tmp = board[1][0]

# dp = [board[0],board[1]]
for i in range(n-1):
    # dp.append([0]*(i+3))
    for j in range(i+1):
        board[i+1][j] = max(tmp+board[i][j], board[i+1][j])
        tmp = board[i+1][j+1]
        # print(f"tmp = {tmp}")
        board[i+1][j+1] = max(board[i][j]+board[i+1][j+1], board[i+1][j+1])        
        
        print(f"i = {i}, j = {j}, tmp = {tmp}")
        print(board)
    tmp = board[i+1][0]
    # print(f"tmp = {tmp}")

print(max(board[n-1]))











end = time.time()
print(f"{end - start:.5f} sec")

