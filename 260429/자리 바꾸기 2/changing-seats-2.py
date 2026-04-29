n, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(k)]

num = [set() for _ in range(n+1)]
seat = [i for i in range(n+1)]

for i in range(1, n+1):
    num[i].add(i)

for _ in range(3):
    for u, v in edges:
        num[seat[u]].add(v)
        num[seat[v]].add(u)

        tmp = seat[u]
        seat[u] = seat[v]
        seat[v] = tmp



for i in range(1, n+1):
    print(len(num[i]))


# Please write your code here.

