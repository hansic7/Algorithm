
n = int(input())
for _ in range(n):
    s = list(input().strip())
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                stack.append(c)
            elif stack[-1] == '(':
                stack.pop()
    if not stack:
        print("YES")
    else:
        print("NO")