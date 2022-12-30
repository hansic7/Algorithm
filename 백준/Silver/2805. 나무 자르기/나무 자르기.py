n,m = map(int, input().split())
board = list(map(int, input().split()))
board.sort(reverse=True)

start = 1
end = max(board)

result = 0

while start <= end:
    mid = (start + end) // 2
    now_m = 0
    for i in board:
        if i - mid > 0:
            now_m += (i - mid)
        else:
            break
    if now_m < m:
        end = mid - 1
    else:
        start = mid + 1
        result = mid
print(result)