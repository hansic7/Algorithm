a, b = map(int, input().split())


def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def sum_prime(a,b):
    cnt = 0
    for i in range(a, b+1):
        if is_prime(i):
            cnt += i

    print(cnt)

sum_prime(a,b)

# Please write your code here.