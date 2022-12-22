from bisect import bisect_left, bisect_right


n,m = 4,6
board =[19,15,10,17]
board.sort()

# n,m =  map(int, input().split())
# board = list(map(int, input().split()))
# board.sort()


def binary(m):
    left, right = 0, n-1
    tmp = 0
    while True:
        tmp = 0
        mid = (right+left) // 2

        for i in range(mid, n):
            if board[mid] > m:
                tmp = tmp - board[mid] + board[i]
        if tmp == m:
            return board[mid]
        if tmp > m:
            left = mid -1
        else: right = mid + 1
        print(tmp)


print(binary(m))