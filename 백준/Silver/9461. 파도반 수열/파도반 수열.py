dp = [0,1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(11, 101):
    dp.append(dp[i-2] + dp[i-3])

for i in range(int(input())):
    print(dp[int(input())])
