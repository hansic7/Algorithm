N = input()
arr = []

dec = 0

for d in N:
    dec = dec * 2 + int(d)

dec *= 17

while True:
    if dec < 2:
        arr.append(dec)    
        break
    arr.append(dec % 2)
    dec //= 2

    
for d in arr[::-1]:
    print(d, end ='')

# Please write your code here.