

n, m = 4,7
board = [20, 15, 10, 17]

n, m = 5,20
board = [4, 42, 40, 26, 46]



board.sort()

m,n = map(int, input().split())
board = list(map(int, input().split()))
board.sort()

start = 1
end = max(board)

result = 0

while start <= end:
    mid = (start + end) // 2
    now_m = 0
    for i in board:
        if i - mid > 0:
            now_m += (i - mid)
    if now_m < m:
        end = mid - 1
    else:
        start = mid + 1
        result = mid
    print(f"mid = {mid} result = {result}, now_m = {now_m}")

print(result)
