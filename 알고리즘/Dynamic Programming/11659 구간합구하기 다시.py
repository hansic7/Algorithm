N,M = 5,3
board = [5, 4, 3, 2, 1]

N, M = map(int, input().split())
board = list(map(int, input().split()))
sum_dp = [0]

for i in range(N):
    sum_dp.append(sum_dp[i]+board[i])

for i in range(M):
    a,b = map(int, input().split())
    print(sum_dp[b] - sum_dp[a-1])
    

    