
n = int(input())
board = list(map(int, input().split()))
board.sort()

comb = set()
mx = max(board)
result = 0
already = []

for i in range(n):
    for j in range(i+1, n):
        
        x = board[i] + board[j]

        start, end = 0, len(board)-1
        while start <= end:
            mid = (start + end) // 2

            if board[mid] == x and mid != i and mid != j and not x in already:
                result += 1
                already.append(x)
                print(f"result = {result}, x = {x}")
                break

            elif x < board[mid]:
                end = mid - 1
            else:
                start = mid + 1

print(result)
