N = int(input())

def dfs(n): 
    if n == 1:
        return 1
    if n == 2:
        return 2
    return dfs(n//3) + dfs(n-1)

print(dfs(N))

# Please write your code here.