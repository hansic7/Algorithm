n, k = map(int, input().split())

arr = [[0] * (n+1)]
for _ in range(n):
    arr.append([0] + list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, n+1):
        arr[i][j] = arr[i-1][j] + arr[i][j-1] + arr[i][j] - arr[i-1][j-1]


ans = 0
for i in range(k, n+1):
    for j in range(k, n+1):
        ans = max(ans, arr[i][j] - arr[i-k][j] - arr[i][j-k] + arr[i-k][j-k])

print(ans)

# Please write your code here.
