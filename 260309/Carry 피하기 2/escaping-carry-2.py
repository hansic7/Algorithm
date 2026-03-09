n = int(input())
arr = [int(input()) for _ in range(n)]

result = 0

def is_carry(n,m,l):
    while n > 0 or m > 0 or l > 0:
        if n % 10 + m % 10 + l % 10 > 10:
            return True
        n = n // 10
        m = m // 10
        l = l // 10
    return False


for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            a,b,c = arr[i], arr[j], arr[k]
            if not is_carry(a,b,c):
                print(a,b,c)
                result = max(result, a+b+c)

print(result)
# Please write your code here.