
N = int(input())

dp = [0] * 1002
dp[1] = 1
dp[2] = 2

if N >= 3:
    for i in range(3, N+1):
        dp[i] = (dp[i-2]) + dp[i-1]
        dp

# print(dp)
print(dp[N]%10007)
