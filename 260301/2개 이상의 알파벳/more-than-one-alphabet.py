A = input()

def dal(s):
    for i in range(1, len(s)):
        if s[0] != s[i]:
            return True
    return  False

if dal(A):
    print('Yes')
else:
    print('No')
        

# Please write your code here.