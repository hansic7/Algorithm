
N, M = map(int, input().split())
s = []
arr = []
for i in range(N+2):
    arr.append(i)

def dfs():
    global s

    if len(s) == M:
        for st in s:
            print(st, end = ' ')
        print()
        return
    

    for i in range(1, N+1):
        s.append(arr[i])
        dfs()
        s.pop()

for i in range(1, N+1):
        s.append(arr[i])
        dfs()
        s.pop()




