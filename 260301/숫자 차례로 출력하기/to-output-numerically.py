n = int(input())

def dfs(n):
    if n == 0:
        return

    dfs(n-1)
    print(n, end = ' ')


def dfs_2(n):
    if n == 0:
        return

    print(n, end = ' ')
    dfs_2(n-1)
    
dfs(n)
print()
dfs_2(n)
    
# Please write your code here.