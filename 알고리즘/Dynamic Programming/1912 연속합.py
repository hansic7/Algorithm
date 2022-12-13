n = 10
n =5
board = [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]
board = [2, 1, -4, 3, 4, -4, 6, 5, -5, 1]
board = [-1, -2, -3, -4, -5]

# n = int(input())
# board = list(map(int, input().split()))
dp = [0] * (n)
# dp[0] = board[0]


for i in range(n):
    dp[i] = max( board[i], board[i]+dp[i-1])
    print(f"i = {i}, dp = {dp}")

print(max(dp))