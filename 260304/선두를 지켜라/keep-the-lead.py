n, m = map(int, input().split())
arr1= [0]
arr2= [0]

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)
    for _ in range(ti):
        arr1.append(arr1[-1] + vi)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)
    for _ in range(ti):
        arr2.append(arr2[-1] + vi)

first = -1
s = 1
while s < len(arr1):
    if arr1[s] > arr2[s]:
        first = 0
        break
    elif arr1[s] < arr2[s]:
        first = 1
        break
    s += 1

result = 0

for i in range(s, len(arr1)):
    cur_first = first
    if arr1[i] > arr2[i]:
        cur_first = 0
    elif arr1[i] < arr2[i]:
        cur_first = 1
    
    if first != cur_first and cur_first != -1:
        result += 1
        first = cur_first

print(result)
# Please write your code here.
