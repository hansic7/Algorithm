N, M = map(int, input().split())
arr = list(map(int, input().split()))

s = []
arr.sort()
visited = [False] * (N+1)

def dfs():
    global s, visited

    if len(s) == M:
        for st in s:
            print(st, end = ' ')
        print()
        return
    
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        s.append(arr[i])
        dfs()
        s.pop()
        visited[i] = False

dfs()