import sys
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
original_x = [p[0] for p in points]
original_y = [p[1] for p in points]

arr = []

res = sys.maxsize

for j in range(1,n-1):
    x = original_x[:j] + original_x[j+1:]
    y = original_y[:j] + original_y[j+1:]
    tmp = 0
    for i in range(1, len(x)):
        tmp += abs(x[i]- x[i-1]) + abs(y[i] - y[i-1])
    res = min(tmp, res)
        
print(res)
# Please write your code here.