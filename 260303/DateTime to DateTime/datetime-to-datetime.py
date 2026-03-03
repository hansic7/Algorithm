a, b, c = map(int, input().split())

def min_(d, h, m):
    h += d * 24
    m += h * 60
    return m

print(min_(a,b,c) - min_(11, 11,11))

# Please write your code here.