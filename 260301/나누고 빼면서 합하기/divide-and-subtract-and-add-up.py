n, m = map(int, input().split())
A = list(map(int, input().split()))

def solve():
    global m
    sol = m

    while m > 1:
        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
        sol += A[m]

    print(sol)

solve()

# Please write your code here.