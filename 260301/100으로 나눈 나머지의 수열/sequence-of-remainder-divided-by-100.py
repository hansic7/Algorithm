N = int(input())

def dfs(n):
    if n == 1: return 2
    if n == 2: return 4

    return dfs(n-1) * dfs(n-2) % 100

print(dfs(N))

# Please write your code here.