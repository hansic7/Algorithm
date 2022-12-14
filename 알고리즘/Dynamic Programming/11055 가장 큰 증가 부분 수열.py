
flag = 0

n = 10
board = [1, 100, 2, 50, 60, 3, 5, 6, 7, 8]

n = int(input())
board = list(map(int, input().split()))
print(board)
dp = [0] * (n)
dp[0] = board[0]
print(dp)
print()

for i in range(1,n):
    if board[i-1] > board[i]:
        j = i
        while board[j-1] >= board[i] and j > 0:
            j -= 1
            # print(f"j = {j} i = {i}")
        dp[i] = dp[j-1] + board[i]
    else:
        dp[i] = dp[i-1] + board[i]
    print(dp)

print()
print(dp)
print(max(dp))