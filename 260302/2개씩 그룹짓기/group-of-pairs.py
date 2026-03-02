n = int(input())
nums = list(map(int, input().split()))

nums.sort()
num = 0

for i in range(n):
    if nums[i] + nums[2*n-1-i] > num:
        num = nums[i] + nums[2*n-1-i]

print(num)

# Please write your code here.
