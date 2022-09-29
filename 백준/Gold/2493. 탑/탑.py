N = int(input())
towers = list(map(int, input().split()))
answer = [0]*N
stack = []

for i in range(N):
    t=towers[i]
    while stack and t > towers[stack[-1]]:
        stack.pop()
    if stack:
        answer[i] = stack[-1]+1
    stack.append(i)
print(' '.join(list(map(str, answer))))