
paran = input()

N = len(paran)
stack = []
cnt = 0

for i in range(N):
    if paran[i] == '(' and paran[i+1] == ')':
        cnt += len(stack)
    elif paran[i-1] == '(' and paran[i] == ")":
        continue
    elif paran[i] == '(':
        stack.append(paran[i])
    elif paran[i] == ')':
        stack.pop()
        cnt += 1
print (cnt)