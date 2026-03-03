n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

arr1 = [0]
arr2 = [0]

for i in range(n):
    if d[i] == 'R':
        tmp = 1
    else:
        tmp = -1
    for _ in range(t[i]):
        arr1.append(arr1[-1] + tmp)

for i in range(m):
    if d2[i] == 'R':
        tmp = 1
    else:
        tmp = -1
    for _ in range(t2[i]):
        arr2.append(arr2[-1] + tmp)

result = -1
for i in range(1, min(len(arr1),len(arr2))):
    if arr1[i] == arr2[i]:
        result = i
        break
print(result)
    
# Please write your code here.