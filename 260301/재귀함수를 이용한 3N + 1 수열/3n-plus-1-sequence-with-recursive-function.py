n = int(input())
cnt = 0

def dfs(n):
    global cnt
    if n == 1: return

    cnt += 1
    if n % 2 == 0:
        return dfs(n // 2)
    else:
        return dfs(n*3 + 1)

dfs(n)
print(cnt)
# Please write your code here.