n, t = map(int, input().split())
arr = list(map(int, input().split()))

res, cnt = 0,0
for i in range(n):
    if arr[i] > t:
        cnt += 1
    else:
        cnt = 0
    res = max(res, cnt)

print(res)
# Please write your code here.