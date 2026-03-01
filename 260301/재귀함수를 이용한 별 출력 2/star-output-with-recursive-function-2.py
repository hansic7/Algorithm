n = int(input())

def dfs(n):
    if n == 0:
        return

    for _ in range(n):
        print('*', end = ' ')
    print()
    dfs(n-1)
    for _ in range(n):
        print('*', end = ' ')
    print()

dfs(n)

# Please write your code here.