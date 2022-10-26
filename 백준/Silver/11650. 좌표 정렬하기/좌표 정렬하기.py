
N = int(input())
board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

board.sort()

for i in range(N):
    print(board[i][0],board[i][1])