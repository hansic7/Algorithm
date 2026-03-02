n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

def start_with(st):
    if len(t) > len(st):
        return False
    for i in range(len(t)):
        if t[i] != st[i]:
            return False
    return True

arr = []

for st in str:
    if start_with(st):
        arr.append(st)

arr.sort()
print(arr[k-1])

# Please write your code here.