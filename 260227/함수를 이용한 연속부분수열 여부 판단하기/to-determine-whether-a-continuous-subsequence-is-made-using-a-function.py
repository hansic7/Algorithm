n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def check(n1,n2,a,b):
    for i in range(n1):
        if a[i] == b[0]:
            tmp_i = i + 1
            for j in range(1, n2):
                if a[tmp_i] != b[j]:
                    break
                tmp_i += 1
            if tmp_i == i + n2:
                return True
    return False

if check(n1,n2,a,b):
    print('Yes')
else:
    print('No')
# Please write your code here.