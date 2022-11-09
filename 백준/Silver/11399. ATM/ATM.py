N = int(input())

board = list(map(int, input().split()))

board.sort()

multi  = N
for i in range(N):
    board[i] *= multi
    multi -= 1

print(sum(board))