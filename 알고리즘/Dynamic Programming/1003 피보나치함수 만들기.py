
N = int(input())

for i in range(N):
    n = int(input())

    cnt_0 = [0] * (n+1)
    cnt_1 = [0] * (n+1)

    def fibo0(n):
        global cnt_0
        if n == 0:
            return (1)
        if n == 1:
            return (0)
        if cnt_0[n] != 0:
            return (cnt_0[n])
        cnt_0[n] = (fibo0(n-1) + fibo0(n-2))
        return(cnt_0[n])

    def fibo_1(n):
        global cnt_1
        if n == 0:
            return (0)
        if n == 1:
            return (1)
        if cnt_1[n] != 0:
            return (cnt_1[n])
        cnt_1[n] = fibo_1(n-1) + fibo_1(n-2)
        return(cnt_1[n])
    
    fibo0(n)
    fibo_1(n)
    print(f"{cnt_0[n]} {cnt_1[n]}")