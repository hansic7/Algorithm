import sys

N = int(sys.stdin.readline())
board = []
for _ in range(N):
    board.append(int(sys.stdin.readline()))

board.sort(reverse=True)
for i in range(N):
    print(board[i])