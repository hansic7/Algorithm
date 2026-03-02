n = int(input())
nums = list(map(int, input().split()))

nums.sort()
for nu in nums:
    print(nu, end = ' ')
print()

nums.sort(reverse = True)
for nu in nums:
    print(nu, end = ' ')
print()



# Please write your code here.
