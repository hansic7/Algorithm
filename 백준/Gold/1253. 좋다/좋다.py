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