a, b = map(int, input().split())
n = input()

arr = []
dec = 0

for d in n:
    dec = dec * a + int(d)

while True:
    if dec < b:
        arr.append(dec)    
        break
    arr.append(dec % b)
    dec //= b

    
for d in arr[::-1]:
    print(d, end ='')

# Please write your code here.
# Please write your code here.