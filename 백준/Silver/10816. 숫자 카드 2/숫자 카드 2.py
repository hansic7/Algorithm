from bisect import bisect_left, bisect_right
N = int(input())
board = list(map(int, input().split()))
board.sort()

m = int(input())
targets = list(map(int, input().split()))

def binary(target):
    return (bisect_right(board, target) - bisect_left(board,target))

for i in range(m):
    print(binary(targets[i]),end=' ')
    