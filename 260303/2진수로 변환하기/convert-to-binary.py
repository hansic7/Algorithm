n = int(input())
arr =[]

while n > 0:
    if n < 2:
        arr.append(n)
        break
    arr.append(n%2)
    n //= 2

for a in arr[::-1]:
    print(a, end = '')

# Please write your code here.