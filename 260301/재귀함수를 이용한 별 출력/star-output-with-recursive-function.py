n = int(input())

def dfs(n):
    if n == 0:
        return

    dfs(n-1)
    print('*' * n)

dfs(n)
# Please write your code here.