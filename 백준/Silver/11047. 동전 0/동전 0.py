N, K = map(int, input().split())
result = 0

coins = []

for i in range(N):
    coins.append(int(input()))
    
for i in range(N-1, -1, -1):
    now = K // coins[i]
    if now:
        result += now
        K -= now*coins[i]

print(result)