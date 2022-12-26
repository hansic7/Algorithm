n = int(input())
board = list(map(int, input().split()))
board.sort()
m = int(input())
s = list(map(int, input().split()))

for i in s:
    start, end = 0, len(board)-1
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if board[mid] == i:
            result = 1
            break
        if i < board[mid]:
            end = mid -1
        else:
            start = mid + 1
    print(result, end= ' ')