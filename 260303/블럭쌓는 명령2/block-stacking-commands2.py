n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

arr = [0] * (n+1)

for s,e in commands:
    for i in range(s, e+1):
        arr[i] += 1

print(max(arr))


# Please write your code here.