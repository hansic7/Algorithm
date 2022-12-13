n = int(input())
board = list(map(int, input().split()))
dp = [0] * (n)


for i in range(n):
    dp[i] = max( board[i], board[i]+dp[i-1])

print(max(dp))