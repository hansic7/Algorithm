from bisect import bisect_left, bisect_right
n = int(input())
board = list(map(int, input().split()))
array = list(set(board))
array.sort()

for i in range(n):
    print(bisect_right(array, board[i])-1, end = ' ')