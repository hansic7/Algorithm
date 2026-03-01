N = int(input())

def dfs(n):
    if n == 1 or n == 2:
        return 1

    return dfs(n-1) + dfs(n-2)


print(dfs(N))
# Please write your code here.