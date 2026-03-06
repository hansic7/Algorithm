import sys

n = int(input())
a = [int(input()) for _ in range(n)]

res = sys.maxsize

for i in range(n):
    tmp = 0
    room_n = i
    dis = 0
    for _ in range(n):
        tmp = tmp + dis * a[room_n]
        dis += 1
        room_n = (room_n + 1) % n
    res = min(tmp, res)

print(res)
# Please write your code here.