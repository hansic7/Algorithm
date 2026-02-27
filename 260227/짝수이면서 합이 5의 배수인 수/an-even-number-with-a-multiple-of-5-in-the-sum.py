n = int(input())

def is_magic_n(n):
    cnt = 0
    while n > 0:
        
        tmp = n % 10
        cnt += tmp

        n = n // 10

    if cnt % 5 == 0:
        print('Yes')
    else:
        print('No')

is_magic_n(n)

# Please write your code here.