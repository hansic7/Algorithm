
# n = 12
# board = [10, 20, 10, 30, 20, 50]
# board = [1, 102, 101, 100, 2, 50, 60, 3, 5, 6, 7, 8]

n = int(input())
board = list(map(int, input().split()))

dp = [0] * n
for i in range(n):
    for j in range(i):
        if board[j] < board[i]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp)+1)


"""
오답코드
n = int(input())
board = list(map(int, input().split()))

dp = [0] * n
dp[0] = 1
-- 여기 한가지 값만 1로 바꿔놓으면  20 10 30 20 50 같은 경우에 문제 생김
왜냐하면 10이 0부터 세기 시작해서 마지막 50에서 2를 출력함
모든 dp 값을 동일한 0혹은 1로 초기화 해놓고
인덱스 0부터 돌리는게 좋음

for i in range(1, n):
    for j in range(i):
        if board[j] < board[i]:
            dp[i] = max(dp[j] + 1, dp[i])
print(max(dp))

"""