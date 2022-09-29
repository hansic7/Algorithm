

N = int(input())
cnt = 0


for i in range(N):
    stack = []
    s = input()
    n = len(s)
    for i in range(n):
        if stack and s[i] == stack[-1]:
            stack.pop()
        else:    
            stack.append(s[i])
        if i == n-1 and not stack:
            cnt += 1

print (cnt)