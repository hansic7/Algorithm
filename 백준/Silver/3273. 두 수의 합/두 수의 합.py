n = int(input())
arr = list(map(int, input().split()))
tg_num = int(input())
result = 0

arr.sort()

left = 0
right = n - 1

while left < right:
    if arr[left] + arr[right] > tg_num:
        right -= 1
    elif arr[left] + arr[right] == tg_num:
        left += 1
        result += 1
    else:
        left += 1

print(result)