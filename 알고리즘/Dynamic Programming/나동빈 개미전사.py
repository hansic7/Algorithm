import copy
n = int(input())
board = list(map(int, input().split()))

dp = copy.deepcopy(board)
for i in range(1,n):
    for j in range(i-1, -1, -1):
        if board[j] < board[i]:
            dp[i] = dp[j] + board[i]
            break
print(max(dp))
print(dp)  