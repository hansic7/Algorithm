
d = [0]*10

def fibo(x):
    if x == 1 or x == 2:
        print(d)
        print()
        return 1
    
    if d[x] != 0:
        print(d)
        print()
        return d[x]
    
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(f"result = {fibo(5)}")