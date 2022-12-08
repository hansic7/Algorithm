
N = int(input())

for i in range(N):
    n = int(input())

    dd = [[0,0] for _ in range(n+1)]

    def fibo(n):
        if n == 0:
            dd[n][0] += 1
            return
        if n == 1:
            dd[n][1] += 1
            return
        fibo(n-2)
        fibo(n-1)

    fibo(n)
    print(f"{dd[0]} {dd[1]}")