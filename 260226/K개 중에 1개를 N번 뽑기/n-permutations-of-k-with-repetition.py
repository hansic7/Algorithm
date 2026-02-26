K, N = map(int, input().split())



def dfs(arr):
    if len(arr) == N:
        for a in arr:
            print(a, end = ' ')
        print()
        return

    for i in range(1, K+1):
        arr.append(i)
        dfs(arr)
        arr.pop()

dfs([])

# Please write your code here.
