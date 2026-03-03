n = int(input())
arr = [int(input()) for _ in range(n)]

cnt,res = 0,0
for i in range(n):
    if i == 0 or arr[i-1] < arr[i]:
        cnt += 1
    else:
        cnt = 1
    res = max(cnt, res)

print(res)
# Please write your code here.