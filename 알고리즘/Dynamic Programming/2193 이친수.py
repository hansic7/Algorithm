dp = [[0,0] for i in range(94)]
dp[0][0] = 1

n = int(input())

for i in range(1, n+1):
    dp[i][0] = dp[i-1][1]
    dp[i][1] = dp[i-1][1]
    dp[i][1] = dp[i][1] + dp[i-1][0]

print(sum(dp[n-1]))
