n, k = map(int, input().split())
arr = list(map(int, input().split()))
dict = {}
ans = 0
# 4 6 5 3 7

for elem in arr:
    diff = k - elem

    if diff in dict:
        ans += dict[diff]
    
    if elem in dict:
        dict[elem] += 1
    else:
        dict[elem] = 1

print(ans)

# Please write your code here.
