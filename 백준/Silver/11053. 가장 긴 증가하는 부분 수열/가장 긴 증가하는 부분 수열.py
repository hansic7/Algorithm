n = int(input())
board = list(map(int, input().split()))

dp = [0] * n
# dp[0] = 1
for i in range(n):
    for j in range(i):
        if board[j] < board[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp)+1)