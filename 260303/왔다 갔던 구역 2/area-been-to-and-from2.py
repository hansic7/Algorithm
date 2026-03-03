n = int(input())
x = []
dir = []
arr = [0] * 1000
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)


xi = 10
d = 1
for i in range(n):
    if dir[i] == 'R':
        tmp_i = xi + x[i]
        d = 1
    else:
        tmp_i = xi - x[i]
        d = -1
    for j in range(xi, tmp_i, d):
        arr[j] += 1
    xi = tmp_i
cnt = 0
for a in arr:
    if a >= 2:
        cnt += 1

print(cnt)
    

# Please write your code here.