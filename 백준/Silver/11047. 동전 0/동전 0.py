n,m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

result = 0
for i in range(n-1, -1, -1):
    if (m // coins [i]) > 0:
        
        result = result + (m//coins[i])
        m = m % coins[i]
print(result)