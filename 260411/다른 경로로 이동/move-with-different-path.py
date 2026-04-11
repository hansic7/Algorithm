import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int, input().split())
    graph[u].append([v,w])
    graph[v].append([u,w])

def diikstra():
    dist = [10e8] * (n+1)
    dist[1] = 0
    pq = []
    heapq.heappush(pq, (0,1))
    
    while pq:
        prev_dist, prev_index = heapq.heappop(pq)

        if dist[prev_index] < prev_dist:
            continue

        for next_index, w in graph[prev_index]:
            next_dist = prev_dist + w
            if dist[next_index] > next_dist:
                dist[next_index] = next_dist
                heapq.heappush(pq, (next_dist, next_index))
    
    return dist


dist_a = diikstra()

for i in range(1, n+1):
    for j in range(len(graph[i])):
        v, w = graph[i][j]
        if dist_a[i] + w == dist_a[v] || dist_a[v] == dist_a[i] + w:
            graph[i][j] = [v, 10e8]


dist_b = diikstra()
if dist_b[n] != 10e8:
    print(dist_b[n])
else:
    print(-1)

# Please write your code here.
