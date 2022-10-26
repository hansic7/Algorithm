
N = int(input())
board = []

for _ in range(N):

    a, b = map(int, input().split())
    board.append([b,a])

board.sort()

for i in range(N):
    print(board[i][1],board[i][0])