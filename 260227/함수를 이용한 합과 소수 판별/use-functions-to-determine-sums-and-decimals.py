a, b = map(int, input().split())

def is_prime(n):
    for i in range(2,n//2 +1):
        if n % i == 0:
            return False
    return True

def all_even(n):
    m = 0
    while n > 0:
        m += n % 10
        n = n // 10
    if m % 2 == 1:
        return False
    return True

def ham(a,b):
    cnt = 0

    for i in range(a, b+1):
        if is_prime(i) and all_even(i):
            cnt += 1
    print(cnt)

ham(a,b)


# Please write your code here.