n = int(input())
arr = [0] + list(map(int, input().split()))

tmp = []
for i in range(1, n+1):
    tmp.append(arr[i])
    if i % 2 != 0:
        tmp.sort()
        print(tmp[(len(tmp))//2], end = ' ')



# Please write your code here.