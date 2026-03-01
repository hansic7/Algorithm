a, b = map(int, input().split())

def solve(a,b):
    if a > b:
        return(a + 25, b * 2)
    else:
        return(a * 2, b + 25)

    
a , b = solve(a,b)
print(a,b)

# Please write your code here.