import heapq
import sys

n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
graph_reverse = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))
    graph_reverse[v].append((u,w))
    
def diikstra(graph):
    pq = []
    dist = [sys.maxsize] * (n+1)
    dist[x] = 0
    heapq.heappush(pq, (0, x))

    while pq:
        prev_dist, prev_index = heapq.heappop(pq)
        
        if dist[prev_index] < prev_dist:
            continue

        for next_index, w in graph[prev_index]:
            if dist[prev_index] + w < dist[next_index]:
                dist[next_index] = dist[prev_index] + w
                heapq.heappush(pq, (dist[prev_index] + w, next_index))

    return dist


dist = diikstra(graph)
dist_reverse = diikstra(graph_reverse)

result = 0
for i in range(1, n+1):
    if i == x:
        continue
    result = max(result, dist[i] + dist_reverse[i])

print(result)


# Please write your code here.
