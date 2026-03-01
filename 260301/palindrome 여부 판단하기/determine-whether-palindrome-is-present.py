A = input()

def plai(a):
    l, r = 0, len(a) - 1

    while l < r:
        if a[l] != a[r]:
            return False
        l += 1
        r -= 1
    return True

if plai(A):
    print('Yes')
else:
    print('No')

# Please write your code here.