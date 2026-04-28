n, k = map(int, input().split())
arr = list(map(int, input().split()))
dict = {}
ans = 0

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        elem = arr[i] + arr[j]
        if elem in dict:
            dict[elem] += 1
        else:
            dict[elem] = 1

for elem in arr:
    diff = k - elem
    if diff in dict:
        ans += dict[diff]

print(ans//3)
# Please write your code here.
