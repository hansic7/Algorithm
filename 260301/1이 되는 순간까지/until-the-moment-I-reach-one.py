N = int(input())

def dfs(n,cnt):
    if n == 1:
        print(cnt)
        return
    
    if n % 2 == 0:
        dfs(n//2, cnt + 1)
    else:
        dfs(n//3, cnt + 1)

dfs(N, 0)

# Please write your code here.