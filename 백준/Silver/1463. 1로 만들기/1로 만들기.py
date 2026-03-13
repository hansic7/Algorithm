
n = int(input())

dp = [-1] * (n+1)

dp[1] = 0

for i in range(2,n+1):
    
    tmp = dp[i-1] + 1
    if i % 2 == 0:
        tmp = min(tmp, dp[i//2]+1)
    if i % 3 == 0:
        tmp = min(tmp, dp[i//3]+1)
    
    dp[i] = tmp

print(dp[n])