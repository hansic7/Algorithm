n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

arr = [0] * 1000
a = []

min = 100 
for s,e in segments:
    if s < min: min = s

if min < 0:
    min = -min

for s,e in segments:
    s += min
    e += min
    for i in range(s, e):
        arr[i] += 1

print(max(arr))

# Please write your code here.