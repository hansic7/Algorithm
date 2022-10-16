
n, m = map(int,input().split())

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range (1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        visited[i] = False



visited = [False] * (n+1)
s = []
dfs()