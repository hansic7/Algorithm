n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# 1 5 7 9 10
# 0 4

for q in queries:
    ans = -1
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == q:
            ans = mid + 1
            break
        elif q <= arr[mid]:
            right = mid-1
        else:
            left = mid+1

    print(ans)
# Please write your code here.
