n, k = map(int, input().split())
a = list(map(int, input().split()))

arr = [a[0]]

for i in range(1, n):
    arr.append(arr[-1] + a[i])

ans = arr[k-1]
for i in range(k, n):
    ans = max(ans, arr[i] - arr[i-k])

print(ans)

# Please write your code here.
