N = int(input())

def dfs(n):
    if n == 0:
        return
    
    print(n, end = ' ')
    dfs(n-1)
    print(n, end = ' ')

dfs(N)
# Please write your code here.