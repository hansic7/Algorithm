a, b, c = map(int, input().split())

def min_(d, h, m):
    h += d * 24
    m += h * 60
    return m

result = min_(a,b,c) - min_(11, 11,11)
if result < 0:
    print(-1)
else:
    print(result)

# Please write your code here.
