import heapq

n,m,x = map(int, input().split())

graph_normal = [[] for _ in range(n+1)]
graph_reverse = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,w = map(int, input().split())

    graph_normal[u].append((v,w))
    graph_reverse[v].append((u,w))


def diikstra(start_index, graph):
    pq = []
    dist = [10e8] * (n+1)

    heapq.heappush(pq, (0, start_index))
    dist[start_index] = 0

    while pq:
        prev_dist, prev_index = heapq.heappop(pq)

        if dist[prev_index] < prev_dist:
            continue

        for next_index, w in graph[prev_index]:
            if prev_dist + w < dist[next_index]:
                dist[next_index] = prev_dist + w
                heapq.heappush(pq, (prev_dist + w, next_index))

    return dist


dist_normal = diikstra(x, graph_normal)
dist_reverse = diikstra(x, graph_reverse)

result = 0
for i in range(1, n+1):
    if i == x:
        continue
    result = max(result, dist_normal[i] + dist_reverse[i])

print(result)