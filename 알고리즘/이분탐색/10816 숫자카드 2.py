from bisect import bisect_left, bisect_right

# N = 10
# m = 8
# board = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
# targets =[10, 9 ,-5, 2, 3, 4, 5, -10]
# board.sort()


N = int(input())
board = list(map(int, input().split()))
board.sort()

m = int(input())
targets = list(map(int, input().split()))

def binary(target):
    return (bisect_right(board, target) - bisect_left(board,target))


for i in range(m):
    print(binary(targets[i]),end=' ')
    