n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

dict = {}

for a in arr:
    if a not in dict:
        dict[a] = 1
    else:
        dict[a] += 1

for num in nums:
    if num in dict:
        print(dict[num], end = ' ')
    else:
        print(0, end = ' ')


# Please write your code here.
