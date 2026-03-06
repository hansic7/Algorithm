n = int(input())
A = list(map(int, input().split()))

res = 10000
for i in range(n):
    tmp = 0
    for j in range(n):
        tmp += A[j] * abs(i-j)
    res = min(res, tmp)

print(res)
# Please write your code here.