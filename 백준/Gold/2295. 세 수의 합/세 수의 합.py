N = int(input())
board = [int(input()) for i in range(N)]
board.sort()

bo_sum = set()
for i in range(N):
    for j in range(N):
        bo_sum.add(board[i]+board[j])

def check():
    for i in range(N-1, -1, -1):
        for j in range(i):
            if (board[i] - board[j]) in bo_sum:
                answer = board[i]
                return answer

print(check())