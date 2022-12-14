
flag = 0

n = 10
board = [1, 100, 2, 50, 60, 3, 5, 6, 7, 8]
board = [3,9,4,9,6,8,7,2,9,8]

# n = int(input())
# board = list(map(int, input().split()))
print(board)
dp = [0] * (n)
dp[0] = board[0]


for i in range(1,n):
    if board[i-1] > board[i]:
        j = i-1
        while board[j] >= board[i] and j >= 1:
            j -= 1
        if j == 0 and board[j] >= board[i]:
            dp[i] = board[i]
        else:
            dp[i] = dp[j] + board[i]
    else:
        dp[i] = dp[i-1] + board[i]
   
print(dp)
print(max(dp))