n,m = map(int,input().split())
board = list(map(int, input().split()))
s = list(map(int, input().split()))
s.sort()

result = []
for i in board:
    start, end = 0, len(s)-1
    flag = 0
    while start <= end:
        mid = (start + end) // 2
        if s[mid] == i:
            flag = 1
            break
        if i < s[mid]:
            end = mid -1
        else:
            start = mid + 1
    if flag == 0:
        result.append(i)

result.sort()
print(len(result))
for i in result:
    print(i, end= ' ')