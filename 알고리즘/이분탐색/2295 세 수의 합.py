N = 5
board = [2,3,5,10,18]


# N = int(input())
# board = [int(input()) for i in range(N)]
board.sort()

bo_sum = set()
for i in range(N):
    for j in range(i, N):  ## 세가지 숫자가 같아도 됨
        bo_sum.add(board[i]+board[j])

def check():
    for i in range(N-1, -1, -1):
        for j in range(i):
            if (board[i] - board[j]) in bo_sum:
                answer = board[i]
                return answer

print(check())