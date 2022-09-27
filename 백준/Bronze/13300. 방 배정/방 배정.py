from math import ceil
a = [[0] * 2 for _ in range(6)]

N, k = map(int, input().split())

for i in range(N):
    pp = (list(map(int, input().split())))
    if pp[0] == 0:
        a[pp[1]-1][0] += 1
    else:
        a[pp[1]-1][1] += 1
    
cnt = 0
for i in range(6):
    for j in range(2):
        cnt += ceil(a[i][j]/k)
print (cnt)