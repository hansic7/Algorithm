
N,M = 5,3
board = [5, 4, 3, 2, 1]
a = [1,2,5]
b= [3,4,5]
a = [0,1,4] ## a,b를 -1하여 저장
b= [2,3,4]

N, M = map(int, input().split())
board = list(map(int, input().split()))
a = []
b = []

for _ in range(M):
    c,d = map(int, input().split())
    dp = 0
    a.append(c-1)
    b.append(d-1)

dp = 0
for i in range(a[0], b[0]+1):
    dp += board[i]
print(dp)

for i in range(1,M):
    if a[i] > a[i-1]:
        for j in range(a[i-1], a[i]):
            dp = dp - board[j]
    if a[i] < a[i-1]:
        for j in range(a[i], a[i-1]):
            dp = dp + board[j]

    if b[i] < b[i-1]:
        for j in range(b[i]+1, b[i-1]+1):
            dp = dp - board[j]
    if b[i] > b[i-1]:
        for j in range(b[i-1]+1, b[i]+1):
            dp = dp + board[j]
    print(f"i = {i}, dp = {dp}")
