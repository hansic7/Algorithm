N = int(input())
s = []
z = 0
result =[]
j = 0
finds = []
answer = 1
for i in range(N):
    finds.append(int(input()))
for i in range(N):
    find = finds[j]
    while z < find:
        z += 1
        s.append(z)
        result.append('+')
    
    if s[-1] == find:
        s.pop()
        result.append('-')
    else:
        print('NO')
        answer = 0
        break
    j += 1
    
if answer != 0:
    result = '\n'.join(result)
    print (result)