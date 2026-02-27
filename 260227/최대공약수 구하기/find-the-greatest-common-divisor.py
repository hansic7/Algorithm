n, m = map(int, input().split())

result = 1
for i in range(min(n,m), 0, -1):
    if n % i == 0 and m % i == 0:
        result = i
        break

print(result)

# Please write your code here.