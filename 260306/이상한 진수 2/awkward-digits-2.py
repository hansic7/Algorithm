a = list(input())

def to_dec(n):
    res = 0
    for b in n:
        res = res * 2 + int(b)
    return res

res = 0
for i in range(len(a)):
    tmp = a[:]
    if tmp[i] == '0':
        tmp[i] = '1'
    else:
        tmp[i] = '0'
    res = max(res, to_dec(tmp))

print(res)
# Please write your code here.