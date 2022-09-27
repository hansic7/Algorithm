aa = list(map(int, input().split()))

def ss(aa):
    a = list(set(aa))
    N = len(a)
    if N == 1:
        print(10000+(max(aa)*1000))
    elif N == 2:
        if aa[0] == aa[1]:
            b = aa[0]
        elif aa[1] == aa[2]:
            b = aa[2]
        else:
            b = aa[0]
        print(1000 + (b*100))
    else:
        print (max(aa)*100)
ss(aa)