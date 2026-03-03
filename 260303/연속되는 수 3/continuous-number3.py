N = int(input())
arr = [int(input()) for _ in range(N)]

cnt, res = 0,0
for i in range(N):
    if i == 0:
        cnt += 1
    elif (arr[i-1] < 0 and arr[i] < 0) or (arr[i-1] > 0 and arr[i] > 0):
        cnt += 1
    else:
        cnt = 1
    res = max(cnt, res)

print(res)

# Please write your code here.