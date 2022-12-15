N = int(input())
dp = [1,2,4]
for i in range(3, 1000001):
    dp.append((dp[i-3]%1000000009)+(dp[i-2]%1000000009)+(dp[i-1]%1000000009))
    
for _ in range(N):
    n = int(input())
        
    print(dp[n-1]%1000000009)