def ss(a,b,c):
    if b == 1:
        return (a%c)
    elif b % 2 == 1:
        return (ss(a, b//2,c))**2*a%c
    else:
        return (ss(a, b//2,c))**2%c
        
a,b,c = map(int,input().split())    
print(ss(a,b,c))