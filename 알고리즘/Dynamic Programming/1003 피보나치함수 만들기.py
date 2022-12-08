
N = int(input())

for i in range(N):
    n = int(input())

    cnt_0 = 0
    cnt_1 = 0

    def fibo(n):
        global cnt_1,cnt_0

        if n == 0:
            cnt_0 += 1
            return
        if n == 1:
            cnt_1 += 1 
            return
        fibo(n-2)
        fibo(n-1)

    fibo(n)
    print(f"{cnt_0} {cnt_1}")