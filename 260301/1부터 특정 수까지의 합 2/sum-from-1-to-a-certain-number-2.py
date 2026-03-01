N = int(input())

def dfs(n):
    if n == 1:
        return 1

    return dfs(n -1) + n

print(dfs(N))

# Please write your code here.