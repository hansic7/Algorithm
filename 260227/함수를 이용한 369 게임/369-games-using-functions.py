a, b = map(int, input().split())



def included(n):
    while n > 0:
        if n % 10 in [3,6,9]:
            return True
        n = n // 10
    return False
    
def is_magic_n(n):
    return n % 3 == 0 or included(n)


cnt = 0
for i in range(a, b+1):
    if is_magic_n(i):
        cnt += 1

print(cnt)
# Please write your code here.