n = int(input())
arr1 = list(map(int, input().split()))
set1 = set(arr1)

m = int(input())
arr2 = list(map(int, input().split()))
set2 = set(arr2)

for elem in arr2:
    if elem in set1:
        print(1, end = ' ')
    else:
        print(0, end = ' ')


# Please write your code here.
