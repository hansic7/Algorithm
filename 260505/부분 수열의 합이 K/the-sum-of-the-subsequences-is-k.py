n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

for i in range(1, n):
    arr[i] = arr[i-1] + arr[i]

for i in range(n):
    for j in range(i):
        if arr[i] == k or arr[i] - arr[j] == k:
            ans += 1
            break
    
print(ans)

# Please write your code here.
