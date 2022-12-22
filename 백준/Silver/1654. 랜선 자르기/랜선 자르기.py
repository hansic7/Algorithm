n, m = map(int, input().split())
board = [int(input()) for i in range(n)]
board.sort()

start, end = 1, max(board)

result = 0
while start <= end and end != 0:
    mid = (start + end) // 2
    now_m = 0
    for i in board:
        now_m += (i // mid)
    if now_m < m:
        end = mid -1
    else:
        start = mid+1
        result = mid

print(result)