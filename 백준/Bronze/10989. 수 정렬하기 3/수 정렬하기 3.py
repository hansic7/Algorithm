import sys

N = int(sys.stdin.readline())
board = [0]*10001
for i in range(N):
    a = int(sys.stdin.readline())
    board[a-1] += 1

for i in range(10001):
    if board[i] != 0:
        for j in range(board[i]):
            print(i+1)