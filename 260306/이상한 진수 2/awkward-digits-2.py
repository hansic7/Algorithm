a = list(input())

for i in range(len(a)):
    if a[i] == '0':
        a[i] = '1'
        break
if a == '1':
    a == '0'
    
a = ''.join(a)

res = 0
for b in a:
    res = res * 2 + int(b)

print(res)
# Please write your code here.
