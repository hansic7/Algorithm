
n = 6
board = [2, 4, -10, 4, -9]
board = [1000, 999, 1000, 999, 1000, 999]

from bisect import bisect_left, bisect_right
# n = int(input())
# board = list(map(int, input().split()))

array = list(set(board))
array.sort()

for i in range(n):
    print(bisect_left(array, board[i]), end = ' ')