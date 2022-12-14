
n = int(input())

dp = [0] * (n+1)

for i in range(1,n):
    # if i == 0:
    #     print(dp[i])
    if i % 5 == 0:
        dp[i*5] = dp[i]+1
    if i % 3 == 0:
        dp[i*3] = dp[i]+1
    if i % 2 == 0:
        dp[i*2] = dp[i]+1
    else:
        dp[i] = dp[i-1] + 1
    print(dp)
print(dp[n-1])