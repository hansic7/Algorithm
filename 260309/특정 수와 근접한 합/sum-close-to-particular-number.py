n, S = map(int, input().split())
arr = list(map(int, input().split()))

total = sum(arr)
diff = S + total

for i in range(n):
    for j in range(i+1, n):
        tmp = abs(S - (total - arr[i] - arr[j]))
        diff = min(tmp, diff)

print(diff)

# Please write your code here.