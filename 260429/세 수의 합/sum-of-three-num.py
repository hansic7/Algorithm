n, k = map(int, input().split())
arr = list(map(int, input().split()))
dict = {}
ans = 0


for elem in arr:
    if elem in dict:
        dict[elem] += 1
    else:
        dict[elem] = 1

for i in range(len(arr)):
    dict[arr[i]] -= 1
    for j in range(i):
        diff = k - arr[i] - arr[j]
        if diff in dict:
            ans += dict[diff]
    

print(ans)
# Please write your code here.
