dp = [0,1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(11, 101):
    dp.append(dp[i-2] + dp[i-3])

n= int(input())
for i in range(n):
    print(dp[int(input())])
