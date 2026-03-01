a, b = map(int, input().split())

def solve(a, b):
    if a > b:
        a *= 2
        b += 10
    else:
        a += 10
        b *= 2
    return (a,b)

a, b = solve(a,b)
print( a,b)

# Please write your code here.