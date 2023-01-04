n,m = 10,4200
coins = [1,5,10,
50,100,500,1000,5000,
10000,
50000]



n,m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

result = 0
for i in range(n-1, -1, -1):
    # print(f"{m//coins[i]}, i = {coins[i]}")
    if (m // coins [i]) > 0:
        
        result = result + (m//coins[i])
        m = m % coins[i]
        # print(f"im in, m = {m}, result = {result}")

print(result)