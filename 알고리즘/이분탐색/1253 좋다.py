n = 10
bbb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# tmp = board[:4] + board[4 + 1:]
# print(tmp)


n = int(input())
bbb = list(map(int, input().split()))
bbb.sort()

result = 0
for i in range(n):
    board = bbb[:i] + bbb[i+1:]
    left = 0
    right = n-2
    while left < right:
        tmp = board[left] + board[right]
        if tmp == bbb[i]:
            result += 1
            break
        elif tmp < bbb[i]:
            left += 1
        else:
            right -= 1

print(result)


















# comb = set()
# mx = max(board)
# result = 0
# already = []

# for i in range(n):
#     for j in range(i+1, n):
        
#         x = board[i] + board[j]

#         start, end = 0, len(board)-1
#         while start <= end:
#             mid = (start + end) // 2

#             if board[mid] == x and mid != i and mid != j and not x in already:
#                 result += 1
#                 already.append(x)
#                 print(f"result = {result}, x = {x}")
#                 break

#             elif x < board[mid]:
#                 end = mid - 1
#             else:
#                 start = mid + 1

# print(result)
