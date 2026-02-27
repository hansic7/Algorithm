y = int(input())

def yoon(n):
    if n % 100 == 0 and n % 400 != 0:
        return False
    return n % 4 == 0

if yoon(y): print('true')
else: print('false')
# Please write your code here.