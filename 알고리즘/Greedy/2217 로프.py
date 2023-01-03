
board = []
n = int(input())
for _ in range(n):
    board.append(int(input()))
board.sort()

result = board[n-1]
j = 2
for i in range(n-2, -1, -1):
    if board[i] * j >= result:
        result = board[i] * j
    j += 1

print(result)