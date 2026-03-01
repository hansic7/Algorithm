a, b, c = map(int, input().split())

def dfs(n):
    if n < 10:
        return n
    
    return n % 10 + dfs(n // 10)

print(dfs(a*b*c))

# Please write your code here.