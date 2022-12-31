
from bisect import bisect_left, bisect_right
m,n = map(int,input().split())

cnvrt_pl = []

for _ in range(m):
    board = list(map(int, input().split()))

    array = board[:]
    array.sort()

    tmp = []
    for i in range(n):
        tmp.append(bisect_left(array, board[i]))
    cnvrt_pl.append(tmp)

result = 0
a = len(cnvrt_pl)
for i in range(a):
    for j in range(i+1,a):
        if cnvrt_pl[i] == cnvrt_pl[j]:
            result += 1

print(result)