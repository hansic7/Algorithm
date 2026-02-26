n, m = map(int, input().split())

def min_mul(n,m):

    max_min = 1
    for i in range(min(n,m), 0, -1):
        if n % i == 0 and m % i == 0:
            max_min = i
            break

    print((n//max_min) * (m//max_min) * max_min)

min_mul(n,m)
# Please write your code here.