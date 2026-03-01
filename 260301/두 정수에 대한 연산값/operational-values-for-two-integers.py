a, b = map(int, input().split())

def solve(a,b):
    if a > b:
        a,b = b,a
    a *= 2
    b += 25
    return(a, b)
a , b = solve(a,b)
print(a,b)

# Please write your code here.