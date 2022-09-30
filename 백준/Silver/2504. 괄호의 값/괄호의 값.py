s = input()
N = len(s)

tmp = 1
cnt = 0
stack = []

for i in range(N):
    
    if s[i] == '(':
        stack.append('(')
        tmp *= 2
        
    elif s[i] == '[':
        stack.append('[')    
        tmp *= 3
        
    elif s[i] == ')':
        if not stack or stack[-1] == '[':
            cnt = 0
            break
        elif s[i-1] == '(':
            cnt += tmp
            stack.pop()
        else:
            stack.pop()
        tmp //= 2
    elif s[i] == ']':
        if not stack or stack[-1] == '(':
            cnt = 0
            break
        elif s[i-1] == '[':
            cnt += tmp
            stack.pop()
        else:
            stack.pop()
        tmp //= 3
        
if stack:
    cnt = 0
print (cnt)