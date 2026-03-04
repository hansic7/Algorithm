N, K, P, T = map(int, input().split())
hand = [tuple(map(int, input().split())) for _ in range(T)]

# 감염여부, 감염시킨횟수
arr = [[0,0] for _ in range((N+1))]
arr[P][0] = 1
hand.sort(key = lambda x : x[0])

for t,x,y in hand:
    if arr[x][0] == 1 and arr[x][1] < K:
        arr[y][0] = 1
        arr[x][1] += 1
    
    if arr[y][0] == 1 and arr[y][1] < K:
        arr[x][0] = 1
        arr[y][1] += 1

for i in range(1, N+1):
    print(arr[i][0], end = '')
# Please write your code here.

# N 개발자 수
# K 감염가능 수
# P 처음 감염자

# t,x,y = 